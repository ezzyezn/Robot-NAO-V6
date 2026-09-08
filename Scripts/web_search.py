from ddgs import DDGS
import requests
from bs4 import BeautifulSoup

# Search only official Teb websites
def search_teb(question):
    queries = [
        f"{question} site:szkolasrednia.teb.pl",
        f"{question} site:teb.pl"
             ]
    
    results = []
    
    for query in queries:
        search_results = DDGS().text(
        query,
        max_results = 3
    )
        
        results.extend(search_results)
    
    return results

# Download the page and extract readable text
def get_page_text(url):
    response = requests.get(
        url,
        timeout=10
    )
    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )
    for tag in soup(["script", "style"]):
        tag.decompose()
        
    text = soup.get_text(
        separator=" ",
        strip=True
    )
    
    return text