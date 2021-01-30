def f(x):
    sum_x = 0
    for i in x:
        sum_x = sum_x + int(i)

    while int(sum_x) > 10:
        sum_y = 0
        for i in str(sum_x):
            sum_y = sum_y + int(i)
        sum_x = sum_y

    return sum_y


x = input('Enter a number: ')
print(f(x))
