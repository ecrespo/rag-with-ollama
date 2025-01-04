import ollama


resp = ollama.generate(
    model="llama3.2",
    prompt="Why the sky is blue?"
)

print(ollama.show("llama3.2"))