text = input("Enter a string: ")

def is_palindrome(text):
    text_lower = text.lower()
    cleaned = ('')
    for char in text_lower:
        if char.isalnum():
            cleaned += char
    if cleaned == text_lower[::-1]:
        return True
    else:
        return False
print(is_palindrome(text))

