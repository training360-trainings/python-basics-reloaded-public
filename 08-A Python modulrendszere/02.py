import random
import os
from modulnev import *
import modulnev as mn
from modulnev import fuggveny1, fuggveny2, valtozo1
import modulnev
Modulok importálása

A Python modulok importálására két módszer áll rendelkezésünkre: az import és a from kulcsszó. Az import kulcsszóval az egész modult importálhatjuk, a from kulcsszóval pedig csak bizonyos függvényeket, osztályokat vagy változókat.

Az import kulcsszóval történő modulimportálás:

python
Copy code
Ez az utasítás betölti az modulnev modult, és lehetővé teszi annak tartalmának használatát a kódunkban. A modulok nevei általában kisbetűvel kezdődnek, és az egész modulnév a fájl
kiterjesztésével egyezik meg. Például, ha van egy "matek" nevű modulunk, akkor az a "matek.py" fájlban található.

A modulok használata során lehetőségünk van csak bizonyos elemeket importálni a modulból a következőképpen:

python
Copy code
Ebben az esetben csak a függvényeket és változókat importáljuk a modulból, amelyeket a programunk használ. Egy másik lehetőség, hogy minden elemet behozzunk a modulból, de egy másik néven használjuk őket:

python
Copy code
Ebben az esetben a "modulnev" modult behozzuk, de a "mn" nevet használjuk az elemekre hivatkozva, például: "mn.fuggveny1()".

Végül, ha a modulban található összes elemet használni szeretnénk, akkor a következő módon importálhatjuk őket:

python
Copy code
Azonban ezt a módszert csak akkor érdemes használni, ha biztosak vagyunk benne, hogy a modulban nincsenek olyan elemek, amelyek azonos nevet viselnek a programunkban található más elemekkel.
Saját modulok készítése
A saját modulok készítése nagyon hasonló a python fájlok írásához. Egyszerűen csak hozzá kell adnunk a modulunkat a programunkhoz az import utasítással.

A moduloknak van egy meghatározott struktúrája, amelyet érdemes követni:

    # modulnev.py

    # importok

    # konstansok
PI = 3.141592653589793

# függvények


def add(a, b):
    return a + b


def substract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b

# osztályok


class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_sum(self):
        return self.x + self.y


Ebben a példában a modulunk neve "modulnev", és van néhány import, konstans, függvény és osztály definiálva.

Egy másik fontos dolog, amire érdemes figyelni a saját modulok készítésekor, hogy a modul tartalmának ne legyen mellékhatása. A modulnak csak függvényeket, osztályokat és konstansokat kell tartalmaznia, amelyek visszatérnek egy é
