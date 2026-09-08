from scraper import load_cache, update_cache_from_irls, split_text
import os
from retrieval import create_embeddings, save_embeddings, load_embeddings

cache_file = "Scripts/school_cache.txt"
embeddings_file = "Scripts/embeddings.json"

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

chunks = split_text(all_text)

if os.path.exists(embeddings_file) and update != "y":
    embeddings = load_embeddings(embeddings_file)
else:
    embeddings = create_embeddings(chunks)
    save_embeddings(embeddings, embeddings_file)
    
print("Chunks:", len(chunks))
print("Embeddings: ", len(embeddings))

