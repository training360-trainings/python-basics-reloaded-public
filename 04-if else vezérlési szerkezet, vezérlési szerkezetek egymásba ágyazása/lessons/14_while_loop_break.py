# is_not_grade = True
# while is_not_grade:
#     grade = input('Kérlek adj meg egy osztályzatot: ')
#     if grade.isdigit() and int(grade) > 0 and int(grade) < 6:
#         print('Ez egy érdemjegy')
#         is_not_grade = False
#     print('Ez nem érdemjegy!')


# while 1:
while True:
    grade = input('Kérlek adj meg egy osztályzatot: ')
    if grade.isdigit() and 0 < int(grade) < 6:
        print('Ez egy érdemjegy')
        break
    print('Ez NEM érdemjegy!')
