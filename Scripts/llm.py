import ollama


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
    print(
        f"Загрузка модели: "
        f"{response['load_duration'] / 1_000_000_000:.2f} с"
    )
    print(
        f"Обработка текста: "
        f"{response['prompt_eval_duration'] / 1_000_000_000:.2f} с"
    )
    print(
        f"Генерация ответа: "
        f"{response['eval_duration'] / 1_000_000_000:.2f} с"
    )
    # Return the generated answer
    return response["message"]["content"]
