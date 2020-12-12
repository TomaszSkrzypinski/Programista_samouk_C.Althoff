# zmienne globalne
x =1
y =2
z =3


def f():
    print(x)
    print(y)
    print(z)


f()

# zmienne lokalne,

def f():
    x = 11
    y = 12
    z = 13
    print(x)
    print(y)
    print(z)


f()


# użycie zmiennej globalnej wewnątrz funkcji

x = 100


def f():
    global x
    x += 1
    print(x)


print(x)
print(f())

# to nie zadziała
def f():
    a = 1
    b = 2
    c = 3

print(a)
print(b)
print(c)


