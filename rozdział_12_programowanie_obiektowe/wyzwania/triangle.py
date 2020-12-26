# zdefiniuj klasę Traingle dysponującą metodą area, która oblicza i zwraca pole trójkąta
# następnie utwórz obiekt triangle, wywołaj metodę area i wyświetl wynik

class Triangle:
    def __init__(self, a, h):
        self.podstawa = a
        self.wysokość = h

    def area(self):
        return 0.5 * self.podstawa * self.wysokość


trinagle = Triangle(12, 18)

print(trinagle.area())