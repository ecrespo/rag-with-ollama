# rag-with-ollama




```
curl http://192.168.10.116:11434/api/generate -d  
'{                                                                     
  "model": "llama3.2",
  "prompt": "Puedes explicar por que el cielo es azul?",
	"stream": false,
  "options": {
    "num_ctx": 4096
  }
}'
```

# Install nltk, tesseract
```
import nltk
nltk.download("punkt_tab")
nltk.download("averaged_perceptron_tagger_end")

```



```
curl http://192.168.10.116:11434/api/chat -d  
'{                                                                     
  "model": "llama3.2",
	"messages": [
		{"role":"user","content":"tell me a fun fact about Venezuela"}],
	"stream": false
}'
```

```
curl http://192.168.10.116:11434/api/generate -d
'{                                                                     
  "model": "llama3.2",
	"prompt": "What color is the sky at different times of the day? Response using JSON",
	"format": "json",
	"stream": false
}'
```

