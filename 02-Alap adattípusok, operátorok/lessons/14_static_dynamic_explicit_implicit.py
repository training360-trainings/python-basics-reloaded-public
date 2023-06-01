# static and explicit: C++
# fordításkor már ismerjk a típust, és a forráskódban is ki van ír
# a változók típusát meg kell adni kell, és a típusok ellenőrzése a fordítási időben történik
# String name = 'Gáll Gergely'

# static and implicit: Java
# fordításkor már ismert a típus, de nincs kiírva
# a változók típusát nem kell megadni, és a típusellenőrzés futási időben történik
name = 'Gáll Gergely'

# dynamic and explicit: Python
# fordításkor nem ismerjük a típust, annak ellenére hogy ki van írva
# a változók típusát egyértelmű módon kell deklarálni, és a típusellenőrzés futási időben történik
# típus annotációról később
vat_rate = int('27')

# dynamic and implicit: JavaScript
# a változók típusa nem kell, hogy egyértelműen módon deklarálva legyen, és a típusellenőrzés is dinamikusan történik a futás során
# a summa típusa a "b" típusától függ
# a = 10
# summa = a + 5
