import requests
from bs4 import BeautifulSoup
import json


def download_page(url):
    response = requests.get(url, timeout=10)

    return response.text


def extract_text(html):
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup(["script", "style"]):
        tag.decompose()

    return soup.get_text(separator=" ", strip=True)


def extract_contact_sections(html):
    text = extract_text(html)

    liceum_location = text.find("Lokalizacja TEB Liceum ")
    technikum_location = text.find("Lokalizacja TEB Technikum ")
    plastyczne_location = text.find("Lokalizacja TEB Liceum Plastyczne")
    domowa_location = text.find("Lokalizacja TEB Edukacja Domowa")

    technikum = text[liceum_location:technikum_location]

    plastyczne = text[technikum_location:plastyczne_location]

    liceum = text[plastyczne_location:domowa_location]

    liceum = liceum.replace("Lokalizacja TEB Liceum Plastyczne", "", 1)

    technikum = technikum.replace("Lokalizacja TEB Liceum", "", 1)

    plastyczne = plastyczne.replace("Lokalizacja TEB Technikum", "", 1)

    return liceum, technikum, plastyczne


def save_text(text, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)


def load_cache(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def update_cache_from_urls(urls, filename):
    all_text = ""
    for url in urls:
        html = download_page(url)

        if "kontakt" in url:
            liceum, technikum, plastyczne = extract_contact_sections(html)

            all_text += "=== SOURCE: KONTAKT ===\n\n"

            all_text += "--- LICEUM ---\n" + liceum + "\n\n"
            all_text += "--- TECHNIKUM ---\n" + technikum + "\n\n"
            all_text += "--- LICEUM PLASTYCZNE ---\n" + plastyczne + "\n\n"
        else:
            text = extract_text(html)

            all_text += "=== SOURCE: NASZA SZKOLA ===\n\n"
            all_text += text + "\n\n"

    save_text(all_text, filename)


def split_text(text, chunk_size=500, overlap=100):
    chunks = []
    step = chunk_size - overlap

    source = ""
    section = ""

    blocks = text.split("\n\n")

    for block in blocks:
        block = block.strip()

        if not block:
            continue

        if block.startswith("=== SOURCE:"):
            source = block
            continue

        if block.startswith("---") and block.endswith("---"):
            section = block
            continue

        for i in range(0, len(block), step):
            chunk = block[i : i + chunk_size]

            chunk_text = ""

            if source:
                chunk_text += source + "\n"

            if section:
                chunk_text += section + "\n"

            chunk_text += chunk

            chunks.append(chunk_text)

    return chunks


def create_documents(urls):
    documents = []

    for url in urls:
        html = download_page(url)

        if "kontakt" in url:
            liceum, technikum, plastyczne = extract_contact_sections(html)

            documents.append({"source": "kontakt", "section": "liceum", "text": liceum})

            documents.append(
                {"source": "kontakt", "section": "technikum", "text": technikum}
            )

            documents.append(
                {
                    "source": "kontakt",
                    "section": "liceum_plastyczne",
                    "text": plastyczne,
                }
            )

        elif "nasza-szkola" in url:
            text = extract_text(html)

            documents.append(
                {"source": "nasza-szkola", "section": "general", "text": text}
            )

    return documents


def split_documents(documents, chunk_size=500, overlap=100):
    chunks = []
    seen = set()
    step = chunk_size - overlap

    for document in documents:
        text = document["text"].strip()

        for i in range(0, len(text), step):
            chunk_text = text[i : i + chunk_size].strip()

            if not chunk_text:
                continue

            key = (document["source"], document["section"], chunk_text)

            if key in seen:
                continue

            seen.add(key)

            chunks.append(
                {
                    "source": document["source"],
                    "section": document["section"],
                    "text": chunk_text,
                }
            )

    return chunks


def save_documents(documents, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(documents, file, ensure_ascii=False, indent=4)


def load_documents(filename):
    with open(filename, "r", encoding="utf8") as file:
        return json.load(file)
