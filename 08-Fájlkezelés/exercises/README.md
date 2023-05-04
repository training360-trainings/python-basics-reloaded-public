# Feladatok

1. Írj egy programot, amely bekéri a felhasználó nevét, majd kiírja ezt az adatot egy szöveges fájlba!
2. Hozz létre egy szöveges fájlt, amelyben egész számok sorozatát tároljuk, vesszővel elválasztva! Írj egy Python függvényt, amely beolvassa a fájlt, majd visszatér az összes szám összegével!
3. Adott egy szöveges fájl, amelyben soronként szerepelnek a nevek. Írj egy Python függvényt, amely beolvassa a fájlt, majd visszatér a nevek listájával, abc-sorrendben rendezve!

```py
total_length = 0
word_count = 0
with open('input.txt', 'r') as file:
    for line in file:
        words = line.strip().split()
        for word in words:
            total_length += len(word)
            word_count += 1
return total_length / word_count if word_count > 0 else 0:
```

Adott egy JSON fájl, amelyben emberek adatai találhatók (vezetéknév, keresztnév, életkoruk). Olvassuk be a fájlt, és számítsuk ki az átlagéletkort!

Adott egy CSV fájl, amelyben diákok osztályzatai találhatók (név, matek, fizika, kémia). Olvassuk be a fájlt, és írjuk ki az összes diák nevét és átlagát az osztályzataikból egy új CSV fájlba!

Adott egy XML fájl, amelyben könyvek adatai találhatók (cím, szerző, kiadó, ár). Olvassuk be a fájlt, és írjuk ki az összes könyv címét és árát egy új XML fájlba, amely csak ezeket az adatokat tartalmazza!

Adott egy CSV fájl, amelyben országok nevei és GDP-jük találhatók. Olvassuk be a fájlt, és írjunk egy függvényt, amely visszaadja az országok átlagos GDP-jét!
