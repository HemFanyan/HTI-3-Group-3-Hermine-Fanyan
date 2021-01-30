def factorial_n(n):
    x = 1
    for i in range(1, 1 + n):
        x = x * i
    return x


n = int(input('Enter a number for factorial: '))
print(factorial_n(n))
