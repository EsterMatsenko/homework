text = input("Enter a text: ")

def correct_sentence(text):
    text = text[0].upper() + text[1:]
    if not text.endswith('.'):
        text += '.'
    return text

print(correct_sentence(text))
