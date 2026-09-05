import ollama ##import the ollama module
import math


def cosine_similarity(a ,b):
    dot_product = 0
    sum_a = 0
    sum_b = 0
    
    for i in range(len(a)):
        dot_product += a[i] * b[i]
        
    for i in range(len(a)):
        sum_a += a[i] ** 2
    
    for i in range(len(b)):
        sum_b += b[i] ** 2
        
    length_a = math.sqrt(sum_a)
    length_b = math.sqrt(sum_b)
    
    return dot_product / (length_a * length_b)


question = input("Enter your message: ") ## prompt the user to enter a message


question_embedding = ollama.embed( ## convert the text into a vector
    model="nomic-embed-text",
    input=question
)["embeddings"][0]


with open("Scripts/school_info.txt", "r", encoding="utf-8") as file: ## school infromation is read from a text file
    school_info = file.read() ## read the content of the file and store it in a variable
    
    
lines = school_info.splitlines() ## split the content of the file into lines


found_info = "" ## variable to store the school information that matches the user's question
best_similarity = 0 ## variable to store the best score for matching lines


for line in lines:
    line_embedding = ollama.embed(
            model="nomic-embed-text",
            input=line
        )["embeddings"][0]
    
    similarity = cosine_similarity(question_embedding,line_embedding)
    print(line, similarity)
    
    if best_similarity < similarity:
        best_similarity = similarity
        found_info = line


print("BEST INFO: ", found_info)
print("BEST SIMILARITY:", best_similarity)

user_message = f"""

Informacje o szkole: {found_info}

Pytanie użytkownika: {question}

""" ##question to be sent to the model, which includes the school information and the user's question

response = ollama.chat( ## call the chat function from the ollama module
    model="llama3.2:3b", ## name of the model we will use
    messages=[
        {   "role": "system", ## role of the message sender, a role for setting rules for the LLM
            "content": """ 
                            Jesteś asystentem AI Technikum TEB Edukacja.

                            Odpowiadaj tylko na pytania dotyczące Technikum TEB Edukacja.

                            Odpowiadaj WYŁĄCZNIE na podstawie informacji,
                            które otrzymasz w wiadomości użytkownika.

                            Jeżeli nie masz wystarczających informacji, odpowiedz:
                            "Nie mam wystarczających informacji na ten temat."

                            Nie wymyślaj informacji.
                        """ ##Instructions for the model to follow when generating a response
            
            },
        
        {"role": "user", ## role of the message sender, this role a standard role for user messages
         "content": user_message ## content of the message, which is the user's question and the school information
            }, 
    ])


print(response['message']['content']) ## print the response from the model