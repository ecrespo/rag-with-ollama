import httpx
import json


url = "http://192.168.10.116:11434/api/generate"

data = {
    "model": "llama3.2",
    "prompt": "Tell me a short story and make it funny",
    "stream": True
}

client = httpx.Client()
response = client.post(url,json=data)

if response.status_code == 200:
    print("Generated text:", end=" ",flush=True)
    for line in response.iter_lines():
        if line:
            result = json.loads(line).get("response","")
            print(result, end="", flush=True)
