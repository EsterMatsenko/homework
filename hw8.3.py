text = input("Enter a list of numbers: ")
some_list = [float(x) for x in text.split()]

def find_unique_value(some_list):
    unique_values = []
    for i in some_list:
        count = some_list.count(i)
        if count == 1:
            unique_values.append(i)
    return unique_values
print(find_unique_value(some_list))