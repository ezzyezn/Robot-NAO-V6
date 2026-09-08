from scraper import load_cache, update_cache_from_irls
import os

cache_file = "Scripts/school_cache.txt"

urls = ["https://szkolasrednia.teb.pl/miasta/d/gdansk/kontakt/",
       "https://szkolasrednia.teb.pl/miasta/d/gdansk/nasza-szkola/"]

update = input("Update cache? (y/n): ")

if os.path.exists(cache_file) and update != "y":
    
    print("Cache already exists")
    
else:  
    
    print("Downloading page...")
    
    update_cache_from_irls(urls, cache_file)
    
    print("Page downloaded")

all_text = load_cache(cache_file)
print(all_text[:1000])

