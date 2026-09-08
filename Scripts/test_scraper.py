import os

from scraper import load_cache, update_cache_from_urls, split_text
from retrieval import (
    create_embeddings,
    save_embeddings,
    load_embeddings,
    find_best_chunk,
    find_top_chunks
)


cache_file = "Scripts/school_cache.txt"
embeddings_file = "Scripts/embeddings.json"


urls = [
    "https://szkolasrednia.teb.pl/miasta/d/gdansk/kontakt/",
    "https://szkolasrednia.teb.pl/miasta/d/gdansk/nasza-szkola/"
    ]


update = input("Update cache? (y/n): ")


if os.path.exists(cache_file) and update != "y":
    print("Cache already exists")
else:  
    print("Downloading page...")
    update_cache_from_urls(urls, cache_file)
    print("Page downloaded")


all_text = load_cache(cache_file)


chunks = split_text(all_text)


if os.path.exists(embeddings_file) and update != "y":
    embeddings = load_embeddings(embeddings_file)
else:
    embeddings = create_embeddings(chunks)
    save_embeddings(embeddings, embeddings_file)
    

question = input("Ask a question: ")


top_chunks = find_top_chunks(
    question,
    chunks,
    embeddings
)


for i, (chunk, similarity) in enumerate(top_chunks, start=1):
    print(f"\nTOP {i}:")
    print(chunk)
    print("SIMILARITY:", similarity)


print("BEST CHUNK: ")
print(top_chunks)
