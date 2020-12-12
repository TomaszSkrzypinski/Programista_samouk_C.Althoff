# funkcja pobiera liczbę i zwraca ją podniesioną do kwadratu

def do_kwadratu():
    """
    :param x: int
    :return: x ** 2
    """
    x = input("podaj liczbę: ")
    x = int(x)
    return x**2

kwadrat = do_kwadratu()

print(kwadrat)


# funkcja pobiera i wyświetla łańcuch znakow

def pobierz_i_wyswietl():
    """
    :param tekst: str
    :print: tekst
    """
    tekst = input("podaj tekst: ")
    print(tekst)


pobierz_i_wyswietl()


# funkcja z trzema wymaganymi i dwoma opcjonalnymi parametrami

def add_param(a, b, c, d = 8, e = 4):
    """
    :param a: int
    :param b: int
    :param c: int
    :param d: int
    :param e: int
    :return: a + b + c + d + e
    """
    return a + b + c + d + e


result = add_param(1, 2, 3)

print(result)


# funkcja pobiera i konwertuje łańcuch znaków na float, z obsługą wyjątków


def get_and_convert():
    try:
        """
        :param x: input
        :print: float(x)
        """
        x = input("podaj liczbę zmiennoprzecinkową: ")
        x = float(x)
        print(x)
    except ValueError:
        print("wprowadzono błędne dane")


get_and_convert()


# kolejne zadanie

def f1(x):
    """
    :param x: int
    :return: x / 2
    """
    return x / 2

def f2(x):
    """
    :param x: int
    :return: x * 4
    """
    x = int(x)
    return x * 4

def operacje_na_dwoch_funkcjach():
    """
    :param x: input
    :print: z
    """
    x = input("podaj liczbę całkowitą: ")
    x = int(x)
    y = f1(x)
    print("wynik pierwszej funkcji wynosi: ", y)
    z = f2(y)
    print("wynik drugiej funkcji wynosi: ", z)


operacje_na_dwoch_funkcjach()


# dodać łańcuch dokumentujący do wszystkich funkcji