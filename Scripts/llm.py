import ollama

# Check if the found information can answer the users question
def check_relevance(question, info):
    response = ollama.chat(
        model = "llama3.2:3b",
        messages=[
            {
                "role": "system",
                "content": """
                            Jesteś filtrem sprawdzającym informacje.

                            Odpowiedz WYŁĄCZNIE:
                            TAK
                            lub
                            NIE

                            Odpowiedz TAK tylko wtedy, gdy podana informacja
                            bezpośrednio lub jednoznacznie pozwala odpowiedzieć na pytanie.

                            Jeżeli trzeba zgadywać, dodawać nowe fakty
                            lub zmieniać znaczenie informacji, odpowiedz NIE.
                            """
            }, {
                "role": "user",
                "content": f"""
                
                Pytanie:
                {question}
                
                Informacja:
                {info}
                
                """
            }
        ]
    )
    
    # Get the models answer
    answer = response["message"]["content"]
    
    # Retunrn True only if the model answered "TAK"
    return answer.strip().upper() == "TAK"


# Generate the final answer for the user
def generate_answer(question, info):
    
    # Create a message with the found information and the users question
    user_message = f"""

        Informacje o szkole: {info}

        Pytanie użytkownika: {question}

        """
    response = ollama.chat( 
    model="llama3.2:3b", 
    messages=[
        {   
         "role": "system", 
            "content": """
                            Jesteś asystentem AI Technikum TEB Edukacja.

                            Odpowiadaj tylko na podstawie informacji podanych w sekcji
                            "Informacje o szkole".

                            Jeżeli informacja odpowiada na pytanie użytkownika,
                            udziel krótkiej i bezpośredniej odpowiedzi.

                            Możesz parafrazować pytanie użytkownika, ale nie zmieniaj faktów.

                            Jeżeli informacji naprawdę nie ma, odpowiedz:
                            "Nie mam wystarczających informacji na ten temat."

                            Nie dodawaj informacji, których nie ma w podanym kontekście.
                        """ 
            
        },
        {
            "role": "user", 
            "content": user_message 
        }, 
    ]
    )
    
    # Return the generated answer
    return response["message"]["content"]