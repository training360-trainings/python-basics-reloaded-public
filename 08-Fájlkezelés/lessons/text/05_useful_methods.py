with open('text2.txt', 'r') as file2:
    # teljes tartalom beolvasása
    print(file2.read())
    # vissza a file elejére
    file2.seek(0)
    # egy sor kiolvasása
    print(file2.readline())
    # vissza a file elejére
    file2.seek(0)
    # soronként bejárás
    for line in file2:
        print(line, end='')
    # vissza a file elejére
    file2.seek(0)
    # két akarakter kiolvasása
    print(file2.read(2))
