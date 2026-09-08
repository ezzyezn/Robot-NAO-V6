import requests
from bs4 import BeautifulSoup


def download_page(url):
    response = requests.get(url, timeout=10)
    
    return response.text


def extract_text(html):
    soup = BeautifulSoup(html, "html.parser")
    
    for tag in soup(["script", "style"]):
        tag.decompose()
        
    return soup.get_text(separator=" ", strip=True)


def extract_contact_sections(html):
    text = extract_text(html)

    liceum_location = text.find("Lokalizacja TEB Liceum ")
    technikum_location = text.find("Lokalizacja TEB Technikum ")
    plastyczne_location = text.find("Lokalizacja TEB Liceum Plastyczne")
    domowa_location = text.find("Lokalizacja TEB Edukacja Domowa")

    technikum = text[liceum_location:technikum_location]

    plastyczne = text[technikum_location:plastyczne_location]

    liceum = text[plastyczne_location:domowa_location]

    liceum = liceum.replace(
    "Lokalizacja TEB Liceum Plastyczne",
    "",
    1
    )

    technikum = technikum.replace(
        "Lokalizacja TEB Liceum",
        "",
        1
    )

    plastyczne = plastyczne.replace(
        "Lokalizacja TEB Technikum",
        "",
        1
    )

    return liceum, technikum, plastyczne


def save_text(text, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)


def load_cache(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def update_cache_from_urls(urls, filename):
    all_text = ""
    for url in urls:
            html = download_page(url)
            
            if "kontakt" in url:
                liceum, technikum, plastyczne = extract_contact_sections(html)
                
                all_text += "=== LICEUM ===\n" + liceum + "\n\n"
                all_text += "=== TECHNIKUM ===\n" + technikum + "\n\n"
                all_text += "=== LICEUM PLASTYCZNE ===\n" + plastyczne + "\n\n"
            else:
                text = extract_text(html)
                
                all_text += text + "\n\n"
    
    save_text(all_text, filename)
    

def split_text(text, chunk_size=500):
    chunks = []
    
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        
        chunks.append(chunk)
        
    return chunks