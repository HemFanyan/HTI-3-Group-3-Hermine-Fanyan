def isPrime(n):
    if n==1:
        return "None"
    elif n>1:
        for i in range(2, n):
            if n % i == 0:
                return "No"

        return "Yes"

    else:
        return "Please enter a natural number"

n = int(input('Enter a natural prime number: '))
print(isPrime(n))
