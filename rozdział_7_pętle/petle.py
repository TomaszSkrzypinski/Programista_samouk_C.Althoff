# pętla for
    # wyświetlenie wszystkich znków z łańcucha

name = "Ted"

for character in name:
    print(character)


    # wyświetlenie elementów listy

shows = ["Jaka to melodai",
         "Spadkobiercy",
         "Familiada"]

for show in shows:
    print(show)


    # wyświetlenie elementów krotki

coms = ("Programowanie",
        "Znajomi",
        "Chillout")

for show in coms:
    print(show)


    # wyświetlenie kluczy słownika

people = {"Fowler":
          "Wzorce projektowe",
          "Knuth":
          "Algorytmy",
          "Stroustrup":
          "C++"}

for character in people:
    print(character)


    # wprowadzanie zmian w danej iterowalnej

tv = ["Jaka to melodai",
         "Spadkobiercy",
         "Familiada"]

i = 0
for show in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1

print(tv)

tv = ["Jaka to melodai",
         "Spadkobiercy",
         "Familiada"]

for i, show in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new

print(tv)

    # modyfikacja i łączenie dwóch pętli

tv = ["Jaka to melodai",
         "Spadkobiercy",
         "Familiada"]

coms = ["Programowanie",
        "Znajomi",
        "Chillout"]

all_shows = []

for show in tv:
    show = show.upper()
    all_shows.append(show)

for show in coms:
    show = show.upper()
    all_shows.append(show)

print(all_shows)


    # funkcja range

for i in range(1, 11):
    print(i)


# pętla while

x = 10

while x > 0:
    print("{}".format(x))
    x -= 1
print("Szczęśliwego nowego roku!")

    # pętla nieskończona

while True:
    print("Witaj, świecie!")

