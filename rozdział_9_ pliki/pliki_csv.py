#!/usr/bin/python
# -*- coding: windows-1250 -*-

import csv


# zapis w pliku csv

with open("st.csv", "w", newline='') as f:
    write = csv.writer(f, delimiter=",")
    write.writerow(["jden", "dwa", "trzy"])
    write.writerow(["cztery", "pięć", "sześć"])


# odczyt pliku csv

with open("st.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))