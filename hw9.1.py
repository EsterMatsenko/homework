import string

text = input("Enter a string: ")
words = input("Enter words separated by a space: ").split()

def popular_words(text, words):
    text_lower = text.lower()
    text_clean = ''.join(char if char not in string.punctuation else ' ' for char in text_lower)
    text_words = text_clean.split()

    result = {}

    for word in words:
        count = text_words.count(word.lower())
        result[word.lower()] = count
    return result

print(popular_words(text, words))