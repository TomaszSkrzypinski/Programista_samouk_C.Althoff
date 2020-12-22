#!/usr/bin/python
# -*- coding: windows-1250 -*-

import csv

# wyświetl zawartość pliku z komputera

path = "C:\Windows\Intel_Chipset_XPVistaWin7_V9301019\AsusSetup.ini"

with open(path, "r") as f:
    print(f.read())


# napisz program który zada pytanie użytkownikowi i zapisze odpowiedź w pliku

path = 'C:\plik_python.txt'

with open(path, "w")as f:
    f.write(input("Jaką mamy porę roku? "))


# napisz program który zapisze w pliku csv listę list,
# każda lista powinna zostać zapisana w osobnym wierszu, a pozycję z listy oddzielone przecinkami

lista = [["Top Gun", "Ocean's Eleven", "Raport mniejszości"],
         ["Titanic", "Ostatni Jedi", "Incepcja"],
         ["Pulp Fiction", "Człowiek w ogniu", "Seksmisja"]]

path = "C:\plik_python.csv"

with open(path, "w", newline='') as f:
    write = csv.writer(f, delimiter=",")
    write.writerow(lista[0])
    write.writerow(lista[1])
    write.writerow(lista[2])
