import ollama ##import the ollama module

content = input("Enter your message: ") ## prompt the user to enter a message

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
         "content": content ## The message we send to the model
            }, 
    ])
print(response['message']['content']) ## print the response from the model