import ollama
import json

def create_embeddings(chunks):
    response = ollama.embed(
        model="qwen3-embedding:0.6b",
        input=chunks
    )
    
    return response["embeddings"]

def save_embeddings(embeddings, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(embeddings,file)