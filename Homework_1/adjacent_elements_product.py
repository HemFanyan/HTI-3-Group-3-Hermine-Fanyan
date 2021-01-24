s = (input('Enter a sequence: '))
s_int=[int(i) for i in s.split()]
product_s = [s_int[i] * s_int[i+1] for i in range(len(s_int)-1)]

print(max(product_s))

