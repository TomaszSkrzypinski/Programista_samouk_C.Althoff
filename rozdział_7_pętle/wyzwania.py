# wyświetl każdy element listy

filmy = ["Noc żywych trupów", "Ekipa", "Rodzina Soprano", "Pamiętnik wampirów"]

for film in filmy:
    print(film)


# wyświetl liczby z zakresu 25-50

for i in range(25, 51):
    print(i)


# wyświetl elemnty listy filmy wraz z indeksami

i = 0
for film in filmy:
    print(film, " Indeks na liście wynosi: ", i)
    i += 1


# pomnóż liczby z jednej listy przez liczby z drugiej listy i zapisz wyniki do trzeciej listy

lista1 = [8, 19, 148, 4]
lista2 = [9, 1, 33, 83]
lista3 = []

for i in lista1:
    for j in lista2:
        lista3.append(i * j)
    lista3.append(" -- ")

print(lista3)


# napisz program z pętlą nieskończoną, kończoną przez wpisanie przycisku "q" oraz listą liczb,
# podczas każdej iteracji proś użytkownika o odgadnięcie liczby z listy oraz wyświetl informację o wyniku zgadywania

liczby = [12, 43, 54, 62]

while input("Wpisz q aby zakończyć.") != "q":
    liczba = input("Zgadnij liczbę: ")
    liczba = int(liczba)
    if liczba in liczby:
        print("Brawo! Zgadłeś!")
    else:
        print("Spróbuj raz jeszcze.")