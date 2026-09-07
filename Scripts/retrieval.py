import ollama
from similarity import cosine_similarity

# Find the best matching information for the users question
def find_best_info(question, lines):
    
    # Convert the users question into an embedding vector
    question_embedding = ollama.embed(
    model="qwen3-embedding:0.6b",
    input=question
)["embeddings"][0]
    
    # Variables for storing the best result
    found_info = ""
    best_similarity = 0
    
    # Check every line from the knowledge base
    for line in lines:
        
        # Convert the current line into an embedding vector
        line_embedding = ollama.embed(
            model="qwen3-embedding:0.6b",
            input=line
        )["embeddings"][0]
    
    # Compare the question vector with the line vector
    similarity = cosine_similarity(
        question_embedding,
        line_embedding
        ) 
    
    # Show similarity for testing
    print(line, similarity)
    
    # Save the line if it is more similar than previous results
    if best_similarity < similarity:
        best_similarity = similarity
        found_info = line
    
    # Return the best information and its similarity score
    return found_info, best_similarity