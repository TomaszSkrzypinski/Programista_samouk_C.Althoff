#!/usr/bin/python
# -*- coding: windows-1250 -*-

import csv

# wy�wietl zawarto�� pliku z komputera

path = "C:\Windows\Intel_Chipset_XPVistaWin7_V9301019\AsusSetup.ini"

with open(path, "r") as f:
    print(f.read())


# napisz program kt�ry zada pytanie u�ytkownikowi i zapisze odpowied� w pliku

path = 'C:\plik_python.txt'

with open(path, "w")as f:
    f.write(input("Jak� mamy por� roku? "))


# napisz program kt�ry zapisze w pliku csv list� list,
# ka�da lista powinna zosta� zapisana w osobnym wierszu, a pozycj� z listy oddzielone przecinkami

lista = [["Top Gun", "Ocean's Eleven", "Raport mniejszo�ci"],
         ["Titanic", "Ostatni Jedi", "Incepcja"],
         ["Pulp Fiction", "Cz�owiek w ogniu", "Seksmisja"]]

path = "C:\plik_python.csv"

with open(path, "w", newline='') as f:
    write = csv.writer(f, delimiter=",")
    write.writerow(lista[0])
    write.writerow(lista[1])
    write.writerow(lista[2])
