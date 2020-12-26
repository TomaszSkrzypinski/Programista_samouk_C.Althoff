class Orange: # nazwy klas piszemy w CamelCase

    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Utworzono!")


or1 = Orange(280, "ciemnopomarańczowy")
or2 = Orange(240, "pomarańczowy")
or3 = Orange(390, "żółty")

print(or1)

print(or1.weight)
print(or1.color)

or1.weight = 650
or1.color = "jasnopomarańczowy"

print(or1.weight)
print(or1.color)