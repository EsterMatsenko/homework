num = int(input('Please enter an integer: '))

print(num, end='')  # Щоб одразу показати початкове число

while num > 9:
    product = 1
    for digit in str(num):
        product *= int(digit)
    num = product
    print(' ->', num, end='')  # Виводимо проміжний результат

print()