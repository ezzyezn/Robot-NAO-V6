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