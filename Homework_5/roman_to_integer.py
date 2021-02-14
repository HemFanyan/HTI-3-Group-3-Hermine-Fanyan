def roman_to_integer(number):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    result = 0

    for i in range(len(number)):
        symbol = number[i]
        if i < len(number) - 1 and roman[symbol] < roman[number[i + 1]]:
            result = result - roman[symbol]
        else:
            result = result + roman[symbol]

    return result


roman_number = input('Enter a roman number: ')

print(roman_to_integer(roman_number))
