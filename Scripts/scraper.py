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

def save_text(text, filename):
    with open (filename, "w", encoding="utf-8") as file:
        file.write(text)

def update_cache(url, filename):
    html = download_page(url)
    text = extract_text(html)
    save_text
    (text, filename)

def load_cache(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()

def update_cache_from_urls(urls,filename):
    all_text = ""
    for url in urls:
            html = download_page(url)
            
            if "kontakt" in url:
                inspect_school_blocks(html)
            
            text = extract_text(html)
            
            all_text += text + "\n\n"
    
    save_text(all_text, filename)
    
def split_text(text,chunk_size=500):
    chunks = []
    
    for i in range(0, len(text), chunk_size):
        chunk = text [i:i + chunk_size]
        
        chunks.append(chunk)
        
    return chunks

def inspect_school_blocks(html):
    soup = BeautifulSoup(html, "html.parser")
    
    for tag in soup.find_all(string=True):
        text = tag.strip()
        
        if text in ["TEB Liceum", "TEB Technikum", "TEB Liceum Plastyczne"]:
            print("TEXT:", text)
            print("TAG:", tag.parent.name)
            print("CLASS:", tag.parent.get("class"))
            print("ID:", tag.parent.get("id"))
            print()