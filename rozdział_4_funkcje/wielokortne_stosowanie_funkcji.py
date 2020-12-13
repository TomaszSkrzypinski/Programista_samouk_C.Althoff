def even_odd(x):
    if x % 2 == 0:
        print("parzysta")
    else:
        print("nieparzysta")


even_odd(4)

even_odd(9)

#-------------------------------------------

def even_odd():
    n = input("Wpisz liczbę: ")
    n = int(n)
    if n % 2 == 0:
        print("liczba jest parzysta")
    else:
        print("liczba jest nieparzysta")


even_odd()
even_odd()
even_odd()