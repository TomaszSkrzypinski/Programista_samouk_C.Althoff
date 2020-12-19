# wyświetlić każdy znak łańcucha "Camus"

camus = "Camus"

print(camus[0])
print(camus[1])
print(camus[2])
print(camus[3])
print(camus[4])


# napisać program pobierający dwa łańcuchy z klawiatury i wstawi je do podanego łańcucha

lancuch = "Wczoraj napisałem {} i wysłałem do {}."

lancuch1 = input("Wprowadź łąńcuch znaków: ")
lancuch2 = input("Wprowadź łąńcuch znaków: ")

gotowy_lancuch = lancuch.format(lancuch1, lancuch2)

print(gotowy_lancuch)


# zmienić pierwszą litere w zdaniu na wielką

zdanie = "aldous Huxley urodził się w 1894 roku."

zdanie_z_wielkiej = zdanie.capitalize()

print(zdanie_z_wielkiej)

    # lub drugi sposób

zdanie_z_wielkiej = zdanie.replace("a", "A")

print(zdanie_z_wielkiej)


# dysponując łańcuchem "Gdzie teraz? Kto teraz? Kiedy, teraz?" wywołać metodę zwracającą listę
# ["Gdzie teraz?", "Kto teraz?", "Kiedy, teraz?"]

lancuch = "Gdzie teraz? Kto teraz? Kiedy, teraz?"
lancuch = lancuch.replace("? ", "?  ")

lista = lancuch.split("  ")

print(lista)


# dyponując listą ["Zwinny", "lis", "przeskoczy", "nad", "leniwym", "psem", "."] przekształcić ją w zdanie

lista = ["Zwinny", "lis", "przeskoczy", "nad", "leniwym", "psem", "."]

zdanie = " ".join(lista)

przedostatni_index = len(zdanie) - 2

zdanie = zdanie[0:przedostatni_index] + zdanie[(przedostatni_index + 1):]

print(zdanie)


# zastąp literę w zdaniu

zdanie = "W czasie suszy szosa sucha"

print(zdanie.replace("s", "$"))


# znjadż ideks litery m w słowie "Hemingway

slowo = "Hemingway"

index = slowo.index("m")

print(index)


# utworzyć potrójny łańcuch znaków na dwa sposoby

slowo = "trzy"

slowo = slowo + " "

potrojne1 = slowo + slowo + slowo

potrojne2 = slowo * 3

print(potrojne1)
print(potrojne2)


# dysponując łańcuchem "Długo na szturm i szaniec poglądał w milczeniu. Na koniec rzekł: 'Stracona'." zwróć wycinek
# obejmujący znaki od początku do pierwszej kropki

zdanie = "Długo na szturm i szaniec poglądał w milczeniu. Na koniec rzekł: 'Stracona'."
indeks_kropki = zdanie.index(".")

wycinek = zdanie[:indeks_kropki + 1]

print(wycinek)

