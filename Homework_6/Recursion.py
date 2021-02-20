s={1,2,3}
def combinations(vals, size = None):
    if size is None:
        size = len(vals)
    if size == 2:
        return vals
    res = []
    for i in vals:
        c = combinations(vals, size - 1)
        for e in c:
            l = [i]
            if isinstance(e, list):
                l.extend(e)
            else:
                l.append(e)
            if l[1] >= i:
                res.append(l)
    return res

print(combinations(s))
print(len(combinations(s)))

# numbers_n = input('Enter n: ')
# number_k = input('Enter k: ')