import ollama


modelfile = """
FROM llama3.2
SYSTEM You are a very smart assistant who knows everything about oceans. You are very succinct and informative.
PARAMETER temperature 0.1
"""

ollama.create(model="knowitall",modelfile=modelfile)

resp = ollama.generate(
    model="knowitall",
    prompt="Why is the ocean so salty?"
)

print(resp["response"])

ollama.delete("knowitall")