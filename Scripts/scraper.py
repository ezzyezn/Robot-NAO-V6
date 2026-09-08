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