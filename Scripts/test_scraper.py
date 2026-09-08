from scraper import download_page, extract_text, save_text
import os

cache_file = "Scripts/school_cache.txt"

url = "https://szkolasrednia.teb.pl/miasta/d/gdansk/kontakt/"

update = input("Update cache? (y/n): ")

if os.path.exists(cache_file) and update != "y":
    
    print("Cache already exists")
    
else:
        
    print("Downloading page...")

    html = download_page(url)
    text = extract_text(html)

    save_text(text, cache_file)

    print("Page downloaded")
