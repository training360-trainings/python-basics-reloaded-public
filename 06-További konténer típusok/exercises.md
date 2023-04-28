Írj egy függvényt, ami egy tuple elemeit cseréli meg. A függvény bemenete egy tuple, ami pontosan két elemet tartalmaz. A függvény visszatérési értéke egy új tuple, ahol az eredeti tuple elemei fel vannak cserélve.
Példa bemenet: (1, 2)
Példa kimenet: (2, 1)

```py
def swap_tuple(t):
    return t[::-1]
```

Írj egy függvényt, ami egy set és egy tuple elemeit fűzi össze. A függvény bemenete egy set és egy tuple. A függvény visszatérési értéke egy új set, amely a bemeneti set és tuple elemeit tartalmazza.
Példa bemenet: {1, 2, 3} és (4, 5, 6)
Példa kimenet: {1, 2, 3, 4, 5, 6}

```py
def merge_set_tuple(s, t):
  return set(list(s) + list(t))
```

Írj egy Python függvényt, amely kap két egész számból álló tuple-t, és visszaadja az összegüket, különbségüket és szorzatukat is egy tuple-ben.
Példa bemenet: (3, 5), (4, 2)
Példa kimenet: (7, 1, 15)

```py
def tuple_ops(t1, t2):
    summa = t1[0] + t2[0]
    diff = t1[0] - t2[0]
    prod = t1[0] * t2[0]
    return (summa, diff, prod)

t1 = (3, 5)
t2 = (4, 2)
print(tuple_ops(t1, t2))  # (7, -1, 12)
```

Írj egy Python függvényt, amely kap egy szótárat és egy kulcsot, majd visszaadja az adott kulcshoz tartozó értéket, vagy ha nincs ilyen kulcs, akkor a "Nincs ilyen kulcs" üzenetet.
Példa bemenet: {"alma": 3, "körte": 4, "barack": 2}, "alma"
Példa kimenet: 3

```py
def get_value(dct, key):
    if key in dct:
        return dct[key]
    else:
        return "Nincs ilyen kulcs"

dct = {"alma": 3, "körte": 4, "barack": 2}
key = "alma"
print(get_value(dct, key))  # 3
```

Írj egy Python függvényt, amely egy szótárat és egy tetszőleges értéket vár bemenetként és visszatér azon kulcs-érték párok listájával, ahol kulcsnál tárolt érték a második paraméterként megadott értékkel egyenlő!
Használj comprehensiot!

```py
def find_key_value_pairs(dct, value):
    return [(key, val) for key, val in dct.items() if val == value]
```

Szótár bővítése
Írj egy Python függvényt, amely bővíti egy szótár kulcsait és értékeit egy másik szótárból. A függvény a következő feladatokat hajtja végre:

Kap egy kulcs-érték párokat tartalmazó szótárat és egy másik kulcs-érték párokat tartalmazó szótárat bemenetként.
Minden kulcs-érték pár hozzáadódik az első szótárhoz, azonban ha a kulcs már létezik az első szótárban, akkor az érték megnő az értéke a második szótárban.
A függvény visszatérési értéke a módosított első szótár.
Feladat megoldása:

```py
def extend_dict(dict1, dict2):
    for key, value in dict2.items():
        if key in dict1:
            dict1[key] += value
        else:
            dict1[key] = value
    return dict1
```

Írj egy függvényt, amely egy szótárból eltávolítja azokat a kulcs-érték párokat, amelyek kulcsa nem szerepel egy megadott kulcsokat tartalmazó listában.
Példa bemenet: {"a": 1, "b": 2, "c": 3}, ["a", "b"]
Példa kimenet: {"a": 1, "b": 2}

```py
def filter_dict(original_dict, keys_to_keep):
    filtered_dict = {}
    for key, value in original_dict.items():
        if key in keys_to_keep:
            filtered_dict[key] = value
    return filtered_dict

original = {"a": 1, "b": 2, "c": 3}
filtered = filter_dict(original, ["a", "b"])

print("Original dict:", original)
print("Filtered dict:", filtered)
```

Írj egy Python függvényt, amely egy szó halmazt kap bemenetként, majd visszatér az összes olyan elemmel, amelyek betűi abc sorrendben állnak. Használj comprehensiont!
Példa bemenet: {'apple', 'banana', 'cat', 'dog', 'elephant', 'frog'}
Példa kimenet: {'elephant', 'frog'}

```py
def alphabetical_set(s):
    return {w for w in s if sorted(w) == list(w)}

words = {'apple', 'banana', 'cat', 'dog', 'elephant', 'frog'}
print(alphabetical_set(words))  # {'elephant', 'frog'}
```

Feladat: Adott két listát, hozz létre egy olyan listát, amely csak azokat az elemeket tartalmazza, amelyek mindkét listában szerepelnek.
Feladat megoldása:

```py
def common_elements(lst1, lst2):
    return list(set(lst1).intersection(lst2))

# példa használat:
lst1 = [1, 2, 3, 4, 5]
lst2 = [3, 4, 5, 6, 7]
print(common_elements(lst1, lst2)) # kimenet: [3, 4, 5]
```

Írj egy Python függvényt, amely egy adott listában megkeresi az összes ismétlődő elemet, majd létrehoz és visszatérít egy halmazt, amely tartalmazza ezeket az elemeket. Például az [1, 2, 3, 2, 4, 3] lista esetén a visszatérített halmaz tartalmazza az 2 és 3 elemeket.

```py
def find_duplicates(lst):
    duplicates = set()
    seen = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return duplicates
```
