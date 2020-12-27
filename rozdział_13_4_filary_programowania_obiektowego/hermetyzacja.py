class rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l


    def area(self):
        return self.width * self.len


class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    def change_data(self, index, n):
        self.nums[index] = n


data_one = Data()

# zmiana danych poprzez bezpośredni dostęp do obiektu
data_one.nums[0] = 100

print(data_one.nums)

data_two = Data()

# zmiana danych przy użyciu metody
data_two.change_data(0, 100)

print(data_one.nums)


# zmienne i metody prywatne - niedostępne w Pythonie,
# pokreślnik na początku nazwy informuje, że nie powinno się używać tej zmiennej/metody

class PublicPrivateExample:

    def __init__(self):
        self.public = "bezpieczne"
        self._unsafe = "niebezpieczne"

    def public_method(self):
        # klient może użyć tej metody
        pass

    def _unsafe_method(self):
        # ta metoda nie powinna
        # być używana poza klasą
        pass