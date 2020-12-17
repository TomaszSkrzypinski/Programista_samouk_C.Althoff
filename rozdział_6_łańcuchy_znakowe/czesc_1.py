# string zajmujący więcej niż 1 linię kodu

string = """wiersz pierwszy \
wiersz drugi \
wiersz trzeci
            """

print(string)


# indeksy

author = "Kafka"

print(author[0])
print(author[1])
print(author[2])
print(author[3])
print(author[4])


# indeksy ujemne

print(author[-4])
print(author[-3])


# konaktacja

print("kot" + "w" + "butach")
print("kot " + "w" + " butach")

# Slice string to remove character at index 5
    # Let’s remove the character at index 5 in above created string object i.e.

strObj = "This is a sample string"

index = 5

if len(strObj) > index:
    strObj = strObj[0 : index : ] + strObj[index + 1 : :]

print(strObj)


#powielanie

print("Puchatek" * 3)

puchatki3 = "Puchatek" * 3

print(puchatki3)


# zmiana wielkości liter

print("Nie pytaj, komu bije dzwon...".upper())

print("TAK TO JEST".lower())

print("historyczny wynik naszej...".capitalize())


# formatowanie - wstawianie tekstu w wyznaczone miejsca

print("William {}".format("Faulkner"))

last = "Faulkner"

print("William {}".format(last))

author = "William Faulkner"

year_born = 1897

print("{} urodził się w {} roku.".format(author, year_born))

n1 = input("Wpisz rzeczownik: ")
v = input("Wpisz czasownik:")
adj = input("Wpisz przymiotnik: ")
n2 = input("Wpisz rzeczownik: ")

r = "The {} {} the {} {}.".format(n1, v, adj, n2)

print(r)