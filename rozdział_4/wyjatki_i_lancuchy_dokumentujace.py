# obsługa wyjątku

try:
    a = input("wpisz liczbę: ")
    b = input("wpisz drugą liczbę: ")
    a = int(a)
    b = int(b)

    print(a / b)

except (ZeroDivisionError, ValueError):
    print("niepoprawne dane wejściowe")


# łańcuchy dokumentujące

def add(x, y):
    """
    :param x: int
    :param y: int
    :return: x + y
    """
    return x + y