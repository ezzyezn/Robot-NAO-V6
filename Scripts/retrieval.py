import ollama
import json
from similarity import cosine_similarity


def create_embeddings(chunks):
    texts = []

    for chunk in chunks:
        text = (
            f"Source: {chunk['source']}\n"
            f"Section: {chunk['section']}\n"
            f"{chunk['text']}"
        )

        texts.append(text)

    response = ollama.embed(
        model="qwen3-embedding:0.6b",
        input=texts
    )

    return response["embeddings"]


def save_embeddings(chunks, embeddings, filename):
    data = {
        "model": "qwen3-embedding:0.6b",
        "chunks": chunks,
        "embeddings": embeddings
    }
    
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def load_embeddings(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def find_best_chunk(question, chunks, embeddings):
    question_embedding = ollama.embed(
        model="qwen3-embedding:0.6b",
        input=question
    )["embeddings"][0]


    best_chunk = ""
    best_similarity = 0
    
    for chunk, chunk_embedding in zip(chunks, embeddings):
        similarity = cosine_similarity(question_embedding,
                                       chunk_embedding)
        if similarity > best_similarity:
            best_similarity = similarity
            best_chunk = chunk
    
    return best_chunk, best_similarity

def find_top_chunks(question, chunks, embeddings, top_k=3):
    question_embedding = ollama.embed(
        model="qwen3-embedding:0.6b",
        input=question
    )["embeddings"][0]
    
    results = []
    
    for chunk, chunk_embedding in zip(chunks, embeddings):
        similarity = cosine_similarity(
            question_embedding,
            chunk_embedding
        )
        
        results.append((chunk, similarity))
        
    results.sort(key=lambda item: item[1], reverse=True)
    return results[:top_k]    