with open("sample.txt", "r") as file:
    text = file.read()

lines = text.splitlines()
words = text.split()
characters = len(text)

print("Number of lines =", len(lines))
print("Number of words =", len(words))
print("Number of characters =", characters)