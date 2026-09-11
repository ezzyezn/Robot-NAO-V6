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
    print("Revelance raw answer:", repr(answer))

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
        model="qwen3:4b-instruct-2507-q4_K_M",
        messages=[
            {
                "role": "system",
                "content": """
                            Masz na imię Tebit. Jesteś przyjaznym robotem.
                            Rozmawiaj naturalnie po polsku i odpowiadaj krótko,
                            zwykle w 1–3 zdaniach.

                            Odpowiadaj swobodnie na powitania, pożegnania,
                            podziękowania oraz proste pytania, takie jak
                            „Jak się nazywasz?” i „Jak się masz?”.

                            Na pytania o szkołę odpowiadaj na podstawie przekazanych
                            informacji. Nie wymyślaj brakujących faktów.
                            Jeśli nie znasz odpowiedzi, powiedz to krótko i uprzejmie.

                            Section oznacza szkołę: liceum, technikum lub liceum_plastyczne.
                            Nie mieszaj ich danych. Jeśli pytanie jest niejasne,
                            poproś o doprecyzowanie.
                            
                            Rozmowa towarzyska obejmuje powitania, pożegnania,
                            podziękowania i krótkie pytania o ciebie.
                            Nie obejmuje pytań o znane osoby, politykę ani wiedzę ogólną.

                            Na takie pytania nie podawaj odpowiedzi rzeczowej.
                            Zamiast tego zaproponuj rozmowę o szkole lub kierunkach.

                            Przykłady naturalnych odpowiedzi:
                            Użytkownik: Jak się nazywasz?
                            Tebit: Mam na imię Tebit!

                            Użytkownik: Jak się masz?
                            Tebit: Dobrze, dzięki! A ty?

                            Użytkownik: Opowiedz o historii starożytnego Rzymu.
                            Tebit: Może porozmawiamy o naszej szkole? Co cię interesuje?
                        """,
            },
            {"role": "user", "content": user_message},
        ],
        options={
            "temperature": 0
        }
    )

    # Return the generated answer
    return response["message"]["content"]
