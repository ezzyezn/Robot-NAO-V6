import os

os.environ.setdefault("OLLAMA_HOST", "http://127.0.0.1:11434")

import ollama


# Generate the final answer for the user
def generate_answer(question, info):

    # Create a message with the found information and the users question
    user_message = (
        f"Dane szkoły:\n{info}\n\n"
        f"Pytanie: {question}"
    )
    response = ollama.chat(
        model="qwen3:4b-instruct-2507-q4_K_M",
        messages=[
            {
                "role": "system",
                "content": (
                    "Jesteś Geraldem, przyjazny robot. "
                    "Mów po polsku, krótko: 1–2 zdania, bez emoji. "
                    "Odpowiadaj na powitania i proste pytania o siebie. "
                    "Fakty o szkole podawaj wyłącznie z danych, "
                    "zgodnie z oznaczeniem szkoły. "
                    "Podane dane są fragmentem oferty, nie pełną listą. "
                    "Na ogólne pytanie o kierunki podaj najwyżej dwa przykłady "
                    "z danych, użyj słowa 'przykładowo' i zapytaj, "
                    "jaka dziedzina interesuje rozmówcę. "
                    "Gdy brak odpowiedzi na dokładne pytanie, "
                    "odpowiedz: Nie mam tej informacji. "
                    "Na inne tematy uprzejmie zaproponuj rozmowę o szkole."
                ),
            },
            {"role": "user", "content": user_message},
        ],
        options={
            "temperature": 0,
            "num_predict": 60,
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
