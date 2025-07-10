import keyword
import string

str = input('Enter a string: ')

if str[0].isdigit():
    print(False)
elif any(c.isupper() for c in str):
    print(False)
elif any(c in string.punctuation and c != '_' for c in str):
    print(False)
elif keyword.iskeyword(str):
    print(False)
elif str.count('_') > 1:
    print(False)
else:
    print(True)

