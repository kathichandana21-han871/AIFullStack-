with open("sample.txt", "r") as file:
    text = file.read()
print(text)
print("No of characters: " , len(text))
print("No of words: " , len(text.split()))
print("No of lines: " , len(text.splitlines()))