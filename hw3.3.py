lst = [1, 2, 3, 4, 5]

if len(lst) == 0:
    part1 = []
    part2 = []

elif len(lst) == 1:
    part1 = [lst[0]]
    part2 = []

else:
    middle = (len(lst) + 1) // 2
    part1 = lst[:middle]
    part2 = lst[middle:]

print(lst, '=>', part1, part2)
