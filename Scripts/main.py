import os

from scraper import create_documents, split_documents, save_documents, load_documents

from retrieval import (
    create_embeddings,
    find_top_chunks,
    save_embeddings,
    load_embeddings,
)

from time import perf_counter

from llm import generate_answer

from speech_to_text import transcribe_audio

from threading import Thread
from nao_bridge import answers, run_server, recordings

from io import BytesIO

documents_file = "Scripts/documents.json"
embeddings_file = "Scripts/embeddings.json"
audio_path = "work/question.wav"

update = input("Update documents? (y/n): ").strip().lower()


urls = [
    "https://szkolasrednia.teb.pl/miasta/d/gdansk/kontakt/",
    "https://szkolasrednia.teb.pl/miasta/d/gdansk/nasza-szkola/",
]


if os.path.exists(documents_file) and update != "y":
    print("Loading documents from cache...")
    documents = load_documents(documents_file)
else:
    print("Downloading documents...")
    documents = create_documents(urls)
    save_documents(documents, documents_file)


chunks = split_documents(documents)

courses = load_documents("Scripts/kierunki.json")

for course in courses:
    for variant in course["variants"]:
        text = (
            f"Kierunek: {course['name']}\n"
            f"Forma nauki: {variant['study_mode']}\n"
            f"Dokumenty do zapisu: "
            f"{variant.get('required_documents', 'Brak informacji')}\n"
            f"Zajęcia: {variant.get('schedule', 'Brak informacji')}\n"
            f"Cena: brak informacji."
        )

        chunks.append(
            {
                "source": "kierunki.json",
                "section": "kierunki",
                "text": text,
            }
        )


print("Kierunki:", len(courses))
print("Documents:", len(documents))
print("Chunks:", len(chunks))


embeddings = None


# Reuse vectors only when both the model and source chunks still match.
if os.path.exists(embeddings_file):
    cached_data = load_embeddings(embeddings_file)

    if (
        isinstance(cached_data, dict)
        and cached_data.get("model") == "qwen3-embedding:0.6b"
        and cached_data.get("chunks") == chunks
        and len(cached_data.get("embeddings", [])) == len(chunks)
    ):
        print("Loading embeddings from cache...")
        embeddings = cached_data["embeddings"]

if embeddings is None:
    print("Creating embeddings...")
    embeddings = create_embeddings(chunks)
    save_embeddings(chunks, embeddings, embeddings_file)

# The HTTP server shares queues with the main processing loop.
Thread(target=run_server, daemon=True).start()

print("\nCześć! Jestem Tebit")
print("Możesz zadawać pytania o szkołę.")

while True:
    print("Czekam na nagranie...")

    # Wait for the next upload without polling the saved WAV file.
    audio_data = recordings.get()

    with BytesIO(audio_data) as audio_file:
        question = transcribe_audio(audio_file)

    print("Rozpoznany tekst:", question)

    if not question:
        continue

    search_start = perf_counter()

    question_lower = question.casefold()

    # Prefer an exact course name before using embedding similarity.
    matched_names = [
        course["name"]
        for course in courses
        if course["name"].casefold() in question_lower
    ]

    if matched_names:
        top_chunks = [
            (chunk, None)
            for chunk in chunks
            if chunk["source"] == "kierunki.json"
            and any(
                chunk["text"].startswith(f"Kierunek: {name}\n")
                for name in matched_names
            )
        ]
    else:
        course_question = any(
            word in question_lower
            for word in ("kierunk", "kurs", "programowan")
        )

        source = "kierunki.json" if course_question else None

        top_chunks = find_top_chunks(
            question,
            chunks,
            embeddings,
            top_k=3,
            source=source,
        )

    print(f"Poszukiwanie: {perf_counter() - search_start:.2f} с")

    context_parts = []

    for chunk, similarity in top_chunks:
        part = (
            f"Source: {chunk['source']}\n"
            f"Section: {chunk['section']}\n"
            f"Text: {chunk['text']}"
        )
        context_parts.append(part)

    context = "\n\n".join(context_parts)

    print("\nTebit myśli...")
    answer_start = perf_counter()

    answer = generate_answer(question, context)

    print(f"Odpowiedź: {perf_counter() - answer_start:.2f} с")
    print("Tebit:", answer)
    answers.put(answer)
