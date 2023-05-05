with open('text.txt', 'r') as file:
    # teljes tartalom beolvasása
    print(file.read())
    # vissza a file elejére
    file.seek(0)
    # egy sor kiolvasása
    print(file.readline())
    # vissza a file elejére
    file.seek(0)
    # soronként bejárás
    for line in file:
        print(line)
    # vissza a file elejére
    file.seek(0)
    # két akarakter kiolvasása
    print(file.read(2))
