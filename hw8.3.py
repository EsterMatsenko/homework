text = input("Enter a list of numbers: ")
some_list = [float(x) for x in text.split()]

def find_unique_value(some_list):
    for i in some_list:
        count = some_list.count(i)
        if count == 1:
            return i
print(find_unique_value(some_list))
