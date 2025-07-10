continue_calc = 'yes'
while continue_calc.lower() in ('y', 'yes'):
    number1 = float(input('Please enter a number: '))
    operation = input('Please enter operation: ')
    number2 = float(input('Please enter another number: '))

    if operation == '/':
        if number2 == 0:
            print('You cant divide by zero')
        else:
            result = number1 / number2
            print(result)

    elif operation == '+':
        print(number1 + number2)

    elif operation == '-':
        print(number1 - number2)

    elif operation == '*':
        print(number1 * number2)
    continue_calc = input("Do you want to continue? (yes/y to continue): ")