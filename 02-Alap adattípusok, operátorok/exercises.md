# Feladatok

**A feladatok megoldása során, ha a feladat szövege külön nem is tér ki rá, az értékeket, számított értékeket mindig tárold el egy-egy változóban!**

Hozz létre két változó. Mindegyiknek az értéke egy tetszőleges int típusú érték. Egy harmadik változóba számold ki a két szám összegét, majd írasd ki ennek a változónak az értékét!

```py
a = 5
b = 7
c = a + b
print(c) # eredmény: 12
```

Hozz létre egy lebegőpontos számot, majd számold ki a négyzetét, írasd ki az értékét!

```py
num = 2.5
square = num ** 2
print(square)
```

Adott két valós szám, írj programot, ami kiszámítja az első szám hatványát a második szám kitevőjével, majd kiírja az eredményt a képernyőre!

```py
a = 2.0
b = 3.0
result = a ** b
print(result)
```

Adott egy szöveges változó, amiben egy mondat található. Írj programot, ami az összes "a" karaktert "e" karakterre cseréli a mondatban, ezt tárold el egy új változóban! Írd ki az új értéket!

```py
sentence = "Az almafa virágzik."
new_sentence = sentence.replace('a", "e')
print(new_sentence)
```

Kérj be két lebegőpontos számot a felhasználótól, majd írasd ki a két szám hányadosát!

```py
num1 = float(input('Kérem, adjon meg egy számot: '))
num2 = float(input('Kérem, adjon meg még egy számot: '))
quotient = num1 / num2
print(quotient)
```

Kérj be egy szöveget a felhasználótól, majd írasd ki a hosszát!

```py
text = input('Kérem, adjon meg egy szöveget: ')
length = len(text)
print(length)
```

Írj egy programot, amely bekéri a felhasználó nevét és korát, majd kiírja az adatait egy mondatban!

```py
name = input('Add meg a neved: ')
age = int(input('Add meg az életkorodat: '))
print(f'A felhasználó neve {name}, és {age} éves.')
```

Írj egy programot, amely kiszámolja egy téglalap területét és kerületét adott oldalhosszak alapján!
Az oldalhosszak értékét a felhasználótól kérd be! Lehet tört szám is. A kerület és terület értékeket írasd ki!

```py
a = float(input('Add meg az "a" oldal hosszát: '))
b = float(input('Add meg a "b" oldal hosszát: '))
area = a *_ b
district = 2 * (a + b)
print(f'Terület: {area}')
print(f'Kerület: {district}')
```

Írj egy programot, amely kiszámolja egy kör területét és kerületét adott sugár alapján! A sugár értékét a a felhasználótól kérd be! Lehet tört szám is. A kerület és terület értékeket írasd ki!

```py
r = float(input('Add meg a kör sugarát: '))
pi = 3.14
area = pi * r ** 2
district = 2 ** pi * r
print(f'Terület: {area}')
print(f'Kerület: {district}')
```

Írj egy programot, amely kiszámolja egy derékszögű háromszög hiányzó oldalát Pitagorasz tételével! A felhasználó adja meg az ismert oldalakat, majd a program határozza meg a hiányzó oldalt és írja ki az eredményt!

```py
a = int(input('Add meg az egyik oldalt: '))
b = int(input('Add meg a másik oldalt: '))
c = (a ** 2 + b ** 2) ** 0.5

print(f'Az ismeretlen oldal hossza: {c}')
```
