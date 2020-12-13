# tworzenie list

fruit = list()

fruit = []

fruit = ["mango", "banan", "gruszka"]

print(fruit)


# dodawanie obiektów do listy - append(dodawany obiekt)

fruit = ["mango", "banan", "gruszka"]
fruit.append("pomelo")
fruit.append("figa")

print(fruit)


# różne dane w liście

random = []
random.append(True)
random.append(100)
random.append(1.1)
random.append("Witaj")

print(random)


# dostęp do obiektów po indeksach

fruit = ["mango", "banan", "gruszka"]

print(fruit[0])
print(fruit[1])
print(fruit[2])


# modyfikacja elementów listy

colors = ["niebieski", "zielony", "czerwony"]

print(colors)

colors[2] = "fioletowy"

print(colors)


# łączenie list

colors1 = ["niebieski", "zielony", "czerwony"]
colors2 = ["fioletowy", "czarny", "purpurowy"]

print(colors1 + colors2)

colors3 = colors1 + colors2

print(colors3)


# usuwanie elementu z listy - pop(indeks elementu lub domyślnie element ostatni)

colors = ["niebieski", "zielony", "czerwony"]

colors.pop(0)

print(colors)


# sprawdzanie obecności elementu w liście - obiekt in lista lub obiekt not in lista

colors = ["niebieski", "zielony", "czerwony"]

print("zielony" in colors)
print("pomarańczowy" not in colors)


# sprawdzanie liczby elementów listy - len(lista)

print(len(colors))


# przykład wykorzystania listy

colors = ["niebieski", "zielony", "czerwony"]

def guess_function():
    guess = input("Zgadnij kolor ")
    if guess in colors:
        print("Zgadłeś")
    else:
        print("Żle, spróbuj jeszcze raz")
        guess_function()

guess_function()
