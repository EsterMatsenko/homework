some_list = input("Enter a list of integers from 0 to 9: ")
some_list = [int(char) for char in some_list]

def add_one(some_list):
    num = int(''.join(str(digit) for digit in some_list))
    num += 1
    return [int(d) for d in str(num)]

print(some_list, "==", add_one(some_list))
