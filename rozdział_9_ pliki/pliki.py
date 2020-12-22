import os

# ścieżka dostępu do pliku

path = os.path.join("programista samouk C.Althoff",
                    "pliki",
                    "st.txt")


# zapis w pliku

st = open("st.txt", "w")
st.write("Cześć... zapisano z Pythona!")
st.close()

# automatyczne zamykanie plików - with open(ścieżka dostępu, tryb dostępu)

with open("st.txt", "w") as f:
    f.write("Cześć...\nzapisano z Pythona!")


# odczyt z plików

with open("st.txt", "r") as f:
    print(f.read())