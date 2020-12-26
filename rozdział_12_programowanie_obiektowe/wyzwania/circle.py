# zdefinuj klasę Circle dysponującą metodą area która oblicza i zwraca pole koła
# następnie utwórz obiekt Circle wyw i wyświetl wynik
# skorystaj z funkcji pi z modułu math

import math

class Circle:

    def __init__(self, r):
        self.promien = r

    def area(self):
        return math.pi * (self.promien ** 2)


circle = Circle(8)

print(circle.area())