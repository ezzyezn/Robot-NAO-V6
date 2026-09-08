from scraper import load_cache, split_text
from retrieval import load_embeddings, find_best_chunk


cache_file = "Scripts/school_cache.txt"
embeddings_file = "Scripts/embeddings.json"


all_text = load_cache(cache_file)
chunks = split_text(all_text)
embeddings = load_embeddings(embeddings_file)


question = input("Ask a question: ")


best_chunk, best_similarity = find_best_chunk(
    question,
    chunks,
    embeddings
)


print("BEST CHUNK:")
print(best_chunk)


print("BEST SIMILARITY:", best_similarity)