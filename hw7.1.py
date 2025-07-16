name = input("Enter your name: ")
age = int(input("Enter your age: "))

def say_hi(name, age):
    return f"Hi. My name is {name}, I'm {age} years old."

print(say_hi(name, age))