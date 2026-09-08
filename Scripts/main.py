# Import functions from other project files
from retrieval import find_best_info
from llm import check_relevance, generate_answer

# Ask the user to enter a question
question = input("Enter your message: ") 

# Minimum similarity required to contiune
minimum_similarity = 0.40 

# Stop if the found information is too differenet from the question
if best_similarity < minimum_similarity: 
    print("Nie mam wystarczających informacji na ten temat.")
    exit()

# Show search results for testing
print("BEST INFO: ", found_info)
print("BEST SIMILARITY:", best_similarity)

# Ask the LLM if the found information really answer the question
is_relevant = check_relevance(question, found_info)

print("RELEVANCE:", is_relevant )

# Stop if the information is not relevant
if not is_relevant:
    print("Nie mam wystarczających informacji na ten temat.")
    exit()

# Generate the final answer using the found information
answer = generate_answer(question, found_info)

print(answer) 