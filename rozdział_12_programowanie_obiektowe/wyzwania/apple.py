# zdefiniuj klasę Apple dysponującą 4 zmiennymi instacyjnymi

class Apple:

    def __init__(self, s, w, k, r):
        self.smak = s
        self.waga = w
        self.kolor = k
        self.rozmiar = r


jablko1 = Apple("słodkie", 125, "czerwone", "średnie")
jablko2 = Apple("słodko-kwaśne", 197, "zielone", "duże")

print(jablko1.kolor)
print(jablko2.rozmiar)