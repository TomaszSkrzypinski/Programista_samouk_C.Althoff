lists = []

rap = ["Kanye West",
       "Jay Z",
       "Eminem",
       "Nas"]

rock = ["Bob Dylan",
        "The Beatles",
        "Led Zeppelin"]

djs = ["Zeds Dead",
       "Tiesto"]

lists.append(rap)
lists.append(rock)
lists.append(djs)

print(lists)

print(lists[1][2])


# modyfikacja listy wewnątrz listy

print(lists[0])

rap.append("Kendrick Lamar")

print(lists[0])

lists[1].append("Roling Stones")

print(rock)


# rózne typy kontenerów w innych kontenerach

    # krotki w liście

locations = []

la = (34.0522, 188.2437)
chicago = (41.8781, 87.6298)

locations.append(la)
locations.append(chicago)

print(locations)


    # listy w krotce

eights = ["Edgar Alan Poe",
          "Charls Dickens"]

nines = ["Hemingway",
         "Fitzgerald",
         "Orwell"]

authors = (eights, nines)

print(authors)


    # słownik w liście i krotce

bday = {"Hemingway":
        "7.21.1899",
        "Fitzgerald":
        "9.24.1896"}

my_list = [bday]

print(my_list)

print(my_list[0]["Fitzgerald"])

my_tuple = (bday,)

print(my_tuple)

print("Hemingway" in my_tuple[0])


    # lista, krotka i słownik jako wartość w innym słowniku

ny = {"lokalizacja":
          (40.7128,
           74.0059),

      "celebryci":
      ["W. Allen",
       "Jay Z",
       "K. Bacon"],

      "fakty":
          {"stan":
           "NY",
           "kraj":
           "Ameryka"}
      }

print(ny)
print(ny["lokalizacja"][0])
print(ny["celebryci"][1])
print(ny["fakty"]["kraj"])