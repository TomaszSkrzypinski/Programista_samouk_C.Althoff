# tworzenie słowników

my_dict = dict()

my_dict = {}

fruits = dict({"agrest": "zielony", "porzeczka" : "czerwony"})

fruits = {"agrest": "zielony", "porzeczka" : "czerwony"}

print(fruits)


# dodawanie par klucz-wartość do słownika i pobieranie wartości na podstawie klucza - słownik[klucz] = wartość

facts = dict()

facts["programowanie"] = "zabawa"
facts["Bill"] = "Gates"
facts["Grunwald"] = "1410"

print(facts["programowanie"])
print(facts["Bill"])
print(facts["Grunwald"])
print(facts)

# sprawdzanie czy w słowniku występuje podany klucz - klucz in słownik lub klucz not in słownik

bill = dict({"Bill Gates" : "charytatywność"})

print("Bill Gates" in bill)
print("Bill Gates" not in bill)


# usuwanie par wartości na podstawie klucza - del słonik[klucz]

books = {"Dracula": "Stoker",
         "1984": "Orwell",
         "Proces": "Kafka"}

print(books)

del books["1984"]

print(books)


# przykład użycia słownika

rhymes = {"1": "niebem",
          "2": "kwa kwa",
          "3": "śni",
          "4": "ordery",
          "5": "cięć"
          }

n = input("Wpisz cyfrę: ")
if n in rhymes:
    print(rhymes[n])
else:
    print("Nie znaleziono")



