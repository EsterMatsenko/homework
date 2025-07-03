import random
lst1 = [random.randint(3, 20) for i in range(random.randint(3, 10))]
lst2 = [lst1[0], lst1[2], lst1[-2]]
print(lst1,"=>", lst2)