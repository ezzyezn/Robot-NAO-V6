import ollama
import json
from similarity import cosine_similarity

def create_embeddings(chunks):
    response = ollama.embed(
        model="qwen3-embedding:0.6b",
        input=chunks
    )
    
    return response["embeddings"]

def save_embeddings(embeddings, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(embeddings,file)

def load_embeddings(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
    
def find_best_chunk(question, chunks, embeddings):
    question_embedding = ollama.embed(
        model="qwen3.embedding:0.6b",
        input=question
    )["embeddings"][0]
    
    best_chunk = 0
    best_simularity = 0
    
    for chunk, chunk_embedding in zip(chunks, embeddings):
        similarity = cosine_similarity(question_embedding,
                                       question_embedding)
        if similarity > best_simularity:
            best_simularity = similarity
            best_chunk = chunk
    
    return best_chunk, best_simularity