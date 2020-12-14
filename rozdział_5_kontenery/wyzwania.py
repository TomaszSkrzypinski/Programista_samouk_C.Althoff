# lista ulubionych zespołów

ulubione_kapele = ["New Model Army", "16 Horsepower", "Wovenhand", "Pink Floyd", "Pixies"]


# lista krotek ze współrzędnymi geograficznymi

lists = [(12.345, 54.321), (67.890, 09.876), (34.567, 76.543)]


# słownik o mnie

ja = {"imię": "Tomasz",
      "nazwisko": "Skrzypiński",
      "miasto": "Swarzędz",
      "ulubiony kolor": "pomarańczowy"}


# program korzystający z powyższego słownika

def pytania_o_mnie():
    pytanie = input("O co chcesz zapytać: ")
    if pytanie in ja:
        print(ja[pytanie])
    else:
        print("Zapytaj o coś innego.")
        pytania_o_mnie()

pytania_o_mnie()


# słownik kojarzący ulubionych muzyków z listami utworów

muzyka = {"New Model Army": ["utwór1", "utwór2", "utwór3"],
          "Pink Floyd": ["utwór1", "utwór2", "utwór3"],
          "Pixies": ["utwór1", "utwór2", "utwór3"]}

print(muzyka["Pixies"])