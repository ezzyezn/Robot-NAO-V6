import ollama ##import the ollama module
import string ##a library for removing unnecessary characters and cleaning the text.
content = input("Enter your message: ") ## prompt the user to enter a message

with open("Scripts/school_info.txt", "r", encoding="utf-8") as file: ## school infromation is read from a text file
    school_info = file.read() ## read the content of the file and store it in a variable
    
lines = school_info.splitlines() ## split the content of the file into lines

clean_content = content.lower().translate(
    str.maketrans("","",string.punctuation) ##removes all punctuation marks.
    )

question_words = clean_content.split() ## split the user's question into words and convert them to lowercase

print(question_words)

stop_words = ["i", "czy", "jest", "w", "się", "sie", "na", "o", "z", "to"] ##remove these words from question_words to make the check faster.

found_info = "" ## variable to store the school information that matches the user's question

best_score = 0 ## variable to store the best score for matching lines

for line in lines:
    score = 0 ## variable to store the score for the current line
    
    for word in question_words:
        if word in stop_words: ## сheck if the word matches a stop word.
            continue
        
        if word in line.lower():## check if any word from the user's question is present in the school information
            score += 1 ## if a match is found, increment the score for the current line
            
    if score > best_score:## if the score for the current line is greater than the best score, update the best score and store the line
        best_score = score
        found_info = line
    
    print(line, score) ## print the current line and its score-0
    

user_message = f"""

Informacje o szkole: {found_info}

Pytanie użytkownika: {content}

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