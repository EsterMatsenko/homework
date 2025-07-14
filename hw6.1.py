import string

letters = input('Please enter two letters seperated by a hyphen: ')

start, end = letters.split('-')

all_letters = string.ascii_letters
start_index = all_letters.index(start)
end_index = all_letters.index(end)

result = all_letters[start_index : end_index + 1]
print(letters,'->', result)
