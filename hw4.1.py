lst1 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
lst2 = []
zero_count = 0

for i in lst1:
    if i != 0:
        lst2.append(i)
    else:
        zero_count += 1

for _ in range(zero_count):
    lst2.append(0)

print(lst1,'->', lst2)