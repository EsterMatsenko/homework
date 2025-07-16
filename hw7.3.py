text = input("Enter a text: ")
some_str = input("Enter some string: ")

def second_index(text, some_str):
    text_lower = text.lower()
    some_str_lower = some_str.lower()

    first_index = text_lower.find(some_str_lower)
    if first_index == -1:
        return None
    second_index = text_lower.find(some_str_lower, first_index + 1)
    if second_index == -1:
        return None
    return second_index

print(second_index(text, some_str))
