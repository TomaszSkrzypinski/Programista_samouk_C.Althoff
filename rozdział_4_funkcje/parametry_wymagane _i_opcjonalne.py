def f(x=2):
    return x**x

print(f())
print(f(4))


def add_it(x, y = 10):
    return x + y


result = add_it(5)
print(result)

result = add_it(5, 5)
print(result)