import sys
def odd_numbers(value):
    result = True
    for number in str(value):
        if int(number) % 2 == 0:
            result = False
            break
    return result

def num_generator(start, stop):
    for i in range(start, stop):
        if odd_numbers(i):
            yield i

if __name__ == '__main__':
    input_start = int(sys.argv[1])
    input_stop = int(sys.argv[2])
    for num in num_generator(input_start, input_stop):
        print(num, end=' ')
    print()