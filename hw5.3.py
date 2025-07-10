import string

str = input("Enter a string: ")

words = str.split()
hashtag = '#'

for word in words:
    clean_word = ''
    for char in word:
        if char not in string.punctuation:
            clean_word += char
    if clean_word:
        hashtag += clean_word.capitalize()
if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)

