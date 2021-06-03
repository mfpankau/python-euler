vals = [0]
total = 0
for x in range(1000):
    if x % 3 == 0:
        vals.append(x)
        continue
    if x % 5 == 0:
        vals.append(x)
for val in vals:
    total = total + val
print(total)
