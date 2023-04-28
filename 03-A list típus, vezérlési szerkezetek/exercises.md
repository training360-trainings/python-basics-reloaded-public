Kérj be egy szöveget a felhasználótól, majd írassuk ki az utolsó karakterét!
Példa bemenet:
Példa kimenet:

```py
text = input("Kérem, adjon meg egy szöveget: ")
last_char = text[-1]
print(last_char)
```

Írj egy Python programot, amely eltávolítja az összes ismétlődő elemet egy listából, és csak a lista egyedi elemeit tartalmazza.
Példa bemenet:
Példa kimenet:

```py
my_list = [1,2,3,4,5,2,3]
uniqe_list = []
for i in my_list:
  if i not in uniqe_list:
    uniqe_list.append(i)
```

Írj egy Python programot, amely kiírja a listában található összes számot, ami 3-mal vagy 5-tel osztható.
Példa bemenet: input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Példa kimenet: [3, 5, 6, 9, 10]

```py
input_list =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([num for num in input_list if num % 3 == 0 or num % 5 == 0])
```

Írj egy Python programot, amely a bemenetként kapott listában az összes páros és páratlan számot két külön listába szétválasztja.
Példa bemenet: input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Példa kimenet:

```py
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odds = [num for num in input_list if num % 2 != 0]
evens = [num for num in input_list if num % 2 == 0]
print(f"odds: {odds}, evens: {evens}")
```

Írj egy Python programot, amely kiírja egy szöveg minden második karakterét.
Példa bemenet: input_string = "abcdefg"
Példa kimenet: "bdf"

```py
input_string =  "abcdefg"
print(input_string[::2])
```

Írj egy Python programot, amely két listát összefűz egyetlen listává úgy, hogy az első lista minden második elemét az második lista megfelelő elemére cseréli.
Példa bemenet: list1 = [1, 2, 3, 4, 5], list2 = [6, 7, 8, 9, 10]
Példa kimenet: [1, 7, 3, 9, 5, 10]

```py
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
result = []
for i, num in enumerate(list1):
  if i % 2 != 0:
    result.append(list2[i-1])
  else:
    result.append(num)
print(result)
```

Adott egy string, amely szóközöket tartalmaz. Írj egy programot, amely eltávolítja a szóköz karaktereket a stringből, majd a string karaktereit fordított sorrendben adja vissza.
Példa bemenet: " Hello, World! "
Példa kimenet: "!dlroW,olleH"

```py
text = " Hello, World! "
text = text.replace(" ", "") # eltávolítjuk a whitespace karaktereket
reversed_text = text[::-1] # visszafordítjuk a stringet
print(reversed_text)
```

Feladat: Adott egy lista, amely számokat tartalmaz. Írj egy programot, amely meghatározza a lista elemeinek összegét a következő feltételek szerint: ha az elem pozitív, akkor az összegbe kerüljön be, ha negatív, akkor ne.
Példa bemenet: [2, -5, 8, -3, 0, -1]
Példa kimenet: 10

```py
lst = [2, -5, 8, -3, 0, -1]
sum = 0
for num in lst:
  if num > 0:
    sum += num

print(sum)
```

Írj egy Python függvényt, amely három egész számot kap bemenetként, és eldönti, hogy ezek az oldalhosszak alkothatnak-e egy háromszöget. Egy logikai True vagy False érték legyen a kimeneten a feltétel kiértékelésétől függően!

Példa bemenet:
a = 3
b = 4
c = 5
Példa kimenet: True

```py
a = 3
b = 4
c = 5

print(a + b > c and a + c > b and b + c > a)
```
