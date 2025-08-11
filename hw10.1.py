def half(x):
    return x//2

def some_gen(begin, n, func):
    current = begin
    for _ in range(n):
        yield current
        current = func(current)

gen = some_gen(100, 7, half)
print(list(gen))