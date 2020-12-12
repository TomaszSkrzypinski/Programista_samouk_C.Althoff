# len - zwraca długość stringa

print(len("Monty"), len('Python'))

print(len('Python'))

# str - przekształca liczby w stringa

str(100)

#int, float - przekształca liczby(stringi) w liczby, oraz liczby int na float i odwrotnie

int("11")

float("123")

print(int("110"))
print(int(11.34))
print(float("110"))
print(float(11))

# input - pobiera dane z klawiatury

age = input("Ile masz lat")
int_age = int(age)

if int_age <21:
    print("Jesteś młody")
else:
    print("Rany... ale jesteś stary")