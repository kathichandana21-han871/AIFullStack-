import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role" : "system",
            "content" : "your teaching to a 5 years child. give the answer in 3-4 lines "
        },
        {
            "role": "user",
            "content":"Explain ml"
        }
    ]
)
print(response["message"]["content"])