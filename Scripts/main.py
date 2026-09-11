import os

from scraper import create_documents, split_documents, save_documents, load_documents

from retrieval import (
    create_embeddings,
    find_top_chunks,
    save_embeddings,
    load_embeddings,
)

from time import perf_counter

from llm import generate_answer


documents_file = "Scripts/documents.json"
embeddings_file = "Scripts/embeddings.json"

update = input("Update documents? (y/n): ").strip().lower()


urls = [
    "https://szkolasrednia.teb.pl/miasta/d/gdansk/kontakt/",
    "https://szkolasrednia.teb.pl/miasta/d/gdansk/nasza-szkola/",
]


if os.path.exists(documents_file) and update != "y":
    print("Loading documents fro cache...")
    documents = load_documents(documents_file)
else:
    print("Downloading documents...")
    documents = create_documents(urls)
    save_documents(documents, documents_file)


chunks = split_documents(documents)


print("Documents:", len(documents))
print("Chunks:", len(chunks))


embeddings = None


if os.path.exists(embeddings_file):
    cached_data = load_embeddings(embeddings_file)

    if (
        isinstance(cached_data, dict)
        and cached_data.get("model") == "qwen3-embedding:0.6b"
        and cached_data.get("chunks") == chunks
        and len(cached_data.get("embeddings", [])) == len(chunks)
    ):
        print("Loading embeddings from cache...")
        embeddings = cached_data["embeddings"]

if embeddings is None:
    print("Creating embeddings...")
    embeddings = create_embeddings(chunks)
    save_embeddings(chunks, embeddings, embeddings_file)


print("\nCześć! Jestem Tebit")
print("Możesz zadawać pytania o szkołę.")

while True:
    question = input("\nTy: ").strip()
    
    if question.lower() == "exit":
        break

    if not question:
        continue
    
    search_start = perf_counter()
    
    top_chunks = find_top_chunks(question, chunks, embeddings, top_k=5)
    
    print(f"Поиск: {perf_counter() - search_start:.2f} с")
    
    context_parts = []
    
    for chunk, similarity in top_chunks:
        part = (
            f"Source: {chunk['source']}\n"
            f"Section: {chunk['section']}\n"
            f"Text: {chunk['text']}"
        )
        context_parts.append(part)
        
    context = "\n\n".join(context_parts)
    
    print("\nTebit myśli...")
    answer_start = perf_counter()

    answer = generate_answer(question, context)

    print(f"Ответ модели: {perf_counter() - answer_start:.2f} с")
    print("Tebit:", answer)
