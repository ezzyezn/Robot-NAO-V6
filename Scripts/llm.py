import ollama


# Check if the found information can answer the users question
def check_relevance(question, info):
    response = ollama.chat(
        model="llama3.2:3b",
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
                            """,
            },
            {
                "role": "user",
                "content": f"""
                
                Pytanie:
                {question}
                
                Informacja:
                {info}
                
                """,
            },
        ],
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
                            Jesteś asystentem informacyjnym szkół TEB w Gdańsku.

                            Odpowiadaj krótko po polsku, wyłącznie na podstawie
                            przekazanych informacji.

                            Odpowiadaj dokładnie na zadane pytanie.
                            Nie zastępuj pytania innym, podobnym pytaniem.

                            Każdy fragment ma oznaczenie Section.
                            liceum, technikum i liceum_plastyczne to różne szkoły.
                            Nie przenoś informacji o osobach i stanowiskach
                            z jednej szkoły do drugiej.

                            Podobieństwo tematu nie oznacza, że fragment zawiera odpowiedź.
                            Sprawdź, czy informacja dotyczy dokładnie osoby, rzeczy,
                            stanowiska i szkoły wskazanych w pytaniu.

                            Jeśli kontekst nie zawiera odpowiedzi na dokładnie zadane
                            pytanie, odpowiedz wyłącznie:
                            Nie mam wystarczających informacji na ten temat.
                        """,
            },
            {"role": "user", "content": user_message},
        ],
    )

    # Return the generated answer
    return response["message"]["content"]
