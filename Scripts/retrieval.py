import ollama
from similarity import cosine_similarity

def find_best_info(question, lines):
    question_embedding = ollama.embed(
    model="qwen3-embedding:0.6b",
    input=question
)["embeddings"][0]
    
    found_info = ""
    best_similarity = 0
    
    for line in lines:
        line_embedding = ollama.embed(
            model="qwen3-embedding:0.6b",
            input=line
        )["embeddings"][0]
    
    similarity = cosine_similarity(question_embedding,line_embedding) 
    
    print(line, similarity)
    
    if best_similarity < similarity:
            best_similarity = similarity
            found_info = line
            
    return found_info, best_similarity