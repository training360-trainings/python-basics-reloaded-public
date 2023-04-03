# Dynamic vs Static: fordítási időben ismert-e a típus

# statikus típusogsság:  a változó típusát a kód írása során határozzuk meg
# a fordító ellenőrzi a típust ha a megadott literál nem az adott típusba tartozik, hibát kapunk
# a változó típusa a kód futása során nem módosul
# int age = 12

# dinamikus típusosság: a változó típusát a program futása során határozzuk meg
age = 12
print(type(age))
