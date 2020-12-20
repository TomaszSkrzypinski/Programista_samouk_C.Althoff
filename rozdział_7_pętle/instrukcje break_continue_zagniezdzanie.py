# instrukcja break

for i in range(0, 100):
    print(i)
    break


qs = ["Jak masz na imię?",
      "Jaki jest twój ulubiony kolor?",
      "Jakie masz zadanie?"]

n = 0

while True:
    print("Wpisz q aby zakończyć")
    a = input(qs[n])
    if a == "q":
        break
    n = (n + 1) % 3


# instrukcja continue

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

i = 1

while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1


# pętle zagnieżdżone

for i in range(1, 3):
    print(i)
    for letter in ["a", "b", "c"]:
        print(letter)

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
added = []

for i in list1:
    for j in list2:
        added.append(i + j)

print(added)

while input("t czy n") != "n":
    for i in range(1, 6):
        print(i)