temperature = 50
humidity = 60
rain = True

if temperature > 30 or humidity < 70 and not rain:
    print('Dry weather')

# not rain            False
# humidity < 70       True
#                     False and True  =  False
# temperature > 30    True
#                     False or True   =   True

if (temperature > 30 or humidity < 70) and not rain:
    print('Dry weather')

# temperature > 30    True
# humidity < 70       True
#                     True or True     =  True
# not rain            False
#                     True and False   =  False
