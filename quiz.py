x = 0
while x < 5:
    print(x)
    x += 1
else:
    print("Vége a ciklusnak")
    x += 1  # HIBA: A ciklusmagon kívül álló utasítás, nem fog lefutni
