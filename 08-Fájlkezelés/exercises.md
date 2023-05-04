Könyvtárak számontartása

Írj egy Python függvényt, amely a következő feladatokat végzi el:

Beolvassa egy könyvtárban található összes fájl nevét és méretét.
Minden fájlnévre, amely végződik ".txt"-vel, létrehoz egy kulcsot a dictionary-ben, és hozzárendel egy értéket, amely a fájl mérete.
A függvény visszatérési értéke a dictionary, amely az összes ".txt" fájlnévhez és mérethez tartozik.
Feladat megoldása:

```py
import os

def count_txt_files(path):
    files_dict = {}
    for file in os.listdir(path):
        if file.endswith(".txt"):
            file_path = os.path.join(path, file)
            files_dict[file] = os.path.getsize(file_path)
    return files_dict
```
