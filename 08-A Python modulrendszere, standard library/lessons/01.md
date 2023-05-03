import math
A modulrendszer bevezetése

A Python modulrendszerrel a kódunkat modulokra oszthatjuk, amelyek lehetővé teszik a funkciók újrafelhasználását és a kód strukturálását. A Python rendelkezik egy beépített modulkészlettel, amely tartalmazza a gyakran használt függvényeket és eszközöket. Emellett a Python lehetővé teszi saját modulok készítését is .

A modulok két típusra oszthatók:

Az előre telepített vagy beépített modulok, amelyeket az alapértelmezett Python környezetben biztosítanak.
A felhasználó által létrehozott modulok, amelyeket saját kódjainkból hozunk létre.
A Python modulrendszerének használatához a következő kulcsszavakat kell ismerni:

import: a modulok importálásához használjuk.
from: egy modulból csak bizonyos függvények, osztályok vagy változók importálásához használjuk.
as: a modulok rövidítéseinek létrehozásához használjuk.
Az importált modulok tartalmát a dir() függvénnyel ellenőrizhetjük.

Példa:

print(dir(math))
Ez a kód az összes math modulban található függvényt és változót listázza ki.

Feladat: Készíts egy modult, amely tartalmaz egy függvényt, amely meghatározza egy kör kerületét adott sugárra.

Megoldás:

python
Copy code

def kerulet(sugar):
return 2 _ math.pi _ sugar

Ez a kód egy kerulet() nevű függvényt hoz létre, amely visszaadja a megadott sugár kör kerületét.
