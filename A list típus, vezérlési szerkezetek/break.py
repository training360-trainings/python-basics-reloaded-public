while True:
    grade = int(input('Kérlek adj meg egy osztályzatot: '))
    if grade > 0 and grade < 6:
        break
    print('Ez nem érdemjegy!')
