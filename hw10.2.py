import re

def first_word(text):
    match = re.search(r"[a-zA-Zа-яА-ЯёЁїЇіІєЄґҐ']+", text)
    return match.group(0) if match else ""

# Ввід від користувача
text = input("Enter a string: ")
print("First word:", first_word(text))
