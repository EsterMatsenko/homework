lst1 = [1, 2, 3, 4, 5, 6]
size = len(lst1)
middle = (size + 1) // 2
part1 = lst1[:middle]
part2 = lst1[middle:]
print(lst1, '=>', part1, part2)

lst2 = [1, 2, 3, 4, 5]
size = len(lst2)
middle = (size + 1) // 2
part1 = lst2[:middle]
part2 = lst2[middle:]
print(lst2, '=>', part1, part2)

lst3 = [1]
size = len(lst3)
middle = (size + 1) // 2
part1 = lst3[:middle]
part2 = lst3[middle:]
print(lst3, '=>', part1, part2)

lst4 = []
size = len(lst4)
middle = (size + 1) // 2
part1 = lst4[:middle]
part2 = lst4[middle:]
print(lst4, '=>', part1, part2)