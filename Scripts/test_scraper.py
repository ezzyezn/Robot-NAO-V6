from scraper import update_cache, load_cache
import os

cache_file = "Scripts/school_cache.txt"

url = ["https://szkolasrednia.teb.pl/miasta/d/gdansk/kontakt/",
       "https://szkolasrednia.teb.pl/miasta/d/gdansk/nasza-szkola/"]

update = input("Update cache? (y/n): ")

if os.path.exists(cache_file) and update != "y":
    
    print("Cache already exists")
    
else:
        
    print("Downloading page...")

    update_cache(url, cache_file)

    print("Page downloaded")

text = load_cache(cache_file)

print(text[:1000])