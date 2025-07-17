lst1 = [num for num in range(100) if num % 3 == 0]
print('List1: ', lst1)
lst2 = [num for num in range(100) if num % 5 == 0]
print('List2: ', lst2)

def common_elements(lst1, lst2):
    intersection = set(lst1) & set(lst2)
    return intersection

print('The intersection is: ', sorted(common_elements(lst1, lst2)))