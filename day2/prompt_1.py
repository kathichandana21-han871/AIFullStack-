import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": "explain ai in 6 lines"
        }
    ]
)

print(response["message"]["content"])
