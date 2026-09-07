import ollama 
from similarity import cosine_similarity
from retrieval import find_best_info
from llm import check_relevance, generate_answer
from knowlegde import load_school_info

question = input("Enter your message: ") 
   
lines = load_school_info()

found_info, best_similarity = find_best_info(question, lines)

minimum_similarity = 0.40 

if best_similarity < minimum_similarity: 
    print("Nie mam wystarczających informacji na ten temat.")
    exit()

print("BEST INFO: ", found_info)
print("BEST SIMILARITY:", best_similarity)

is_relevant = check_relevance(question, found_info)

print("RELEVANCE:", is_relevant )

if not is_relevant:
    print("Nie mam wystarczających informacji na ten temat.")
    exit()

answer = generate_answer(question, found_info)

print(answer) 