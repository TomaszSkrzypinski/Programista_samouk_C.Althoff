# zdefinuj klasę Hexagon dysponującą metodą calculate_perimeter która oblicza i zwraca obwód sześciokąta
# nastepnie utwórz obiekt tej klasy, wywołaj metodę calc... i wyświetl wynik

class Hexagon:
    def __init__(self, a):
        self.bok = a

    def calculate_perimeter(self):
        return self.bok * 6


hexagon = Hexagon(5)

print(hexagon.calculate_perimeter())