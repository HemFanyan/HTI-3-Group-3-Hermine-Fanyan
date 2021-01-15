year = int(input('Enter a year: '))

century = year//100

if year % 100 != 0:
    print(century+1)

else:
    print (century)


