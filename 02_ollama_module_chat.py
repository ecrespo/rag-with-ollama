import ollama

response = ollama.list()
models = response.get("models")
# for model in models:
#     print(model["model"])

resp = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": "Why is the sky blue?"
        }
    ]
)
print(resp["message"]["content"])