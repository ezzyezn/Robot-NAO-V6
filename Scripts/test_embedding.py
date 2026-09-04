import ollama

text = "Dyrektorem szkoły jest Iwona Białopiotrowicz"

response = ollama.embed(
    model="nomic-embed-text",
    input=text
)

print(response["embeddings"][0])