# dzielenie łańuchów na listy

print("Hej.Siema!".split("."))


# metoda join

first_thre = "abc"

print("+".join(first_thre))

words = ["Zwinny", "lis", "przeskoczy", "nad", "leniwym", "psem", "."]

one = "".join(words)

one_string = " ".join(words)

print(one)
print(one_string)


# usuwanie odstępów

s = "    To    "

s = s.strip()

print(s)


# zastępowanie

equ = "Ostry wicher mrozi."

equ = equ.replace("r", "@")

print(equ)


# znajdowanie indeksu

print("imperialny".index("r"))

try:
    print("imperialny".index("z"))
except:
    print("Nie znaleziono znaku.")


# metoda in

print("Kot" in "Kot w butach")

print("Pies" not in "Kot w butach")


# zabezpieczanie znaków specjalnych - \

print("Odpowiedziała mu: \"Owszem.\"")

print('Odpowiedziała mu: "Owszem."')

print("Odpowiedziała mu: 'Owszem.'")


# znak nowego wiersza - \n

print("Wiersz1\nwiersz2\nwiersz3")


# wycinki

fict = ["Clavel", "Orwell", "Camus", "Huxley", "Austin"]

print(fict[0:3])

ivan = "A żyć tak na skraju zguby trzeba samotnie"

print(ivan[0:10])
print(ivan[26:41])

print(ivan[:19])

print(ivan[26:])

print(ivan[:])