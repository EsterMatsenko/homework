lst = [0, 1, 7, 2, 4, 8]

if len(lst) == 0:
    result = 0
    print(result)
else:
    sum = 0
    for i in range(0, len(lst), 2):
        sum += lst[i]
    result = sum * lst[-1]
print(lst, "=>", result)