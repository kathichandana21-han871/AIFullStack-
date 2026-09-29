import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content":"Explain AI in 2 lines and three main types of ai in bullet points"
        }
    ]
)
print(response["message"]["content"])