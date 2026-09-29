import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role" : "system",
            "content" : "Give the answers in 3-4 lines only"
        },
        {
            "role": "user",
            "content":"Explain ml"
        }
    ]
)
print(response["message"]["content"])