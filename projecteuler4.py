text = ''
palis = []

def filterSize(val):
    return int(val)

for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        text = str(i * j)
        if text == text[::-1]:
            if not text in palis:
                palis.append(text)
palis.sort(key=filterSize)

vals = []
for x in range(999, 99, -1):
    if int(palis[len(palis) - 1]) % x == 0:
        vals.append(x)
        vals.append(int(int(palis[len(palis) - 1]) / x))
        break
print('solution: ' + str(palis[len(palis) - 1]) + ' is ' + str(vals[0]) + ' * ' + str(vals[1]))
