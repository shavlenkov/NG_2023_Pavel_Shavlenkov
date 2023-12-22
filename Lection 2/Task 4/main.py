letters = ["a", "e", "i", "o", "u"]

text = input("Enter text in English:");

new_text = ""

for letter in text:
    if letter.lower() in letters:
        new_text += letter

print(new_text)