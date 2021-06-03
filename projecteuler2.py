fib = [1, 2]
i = 1
while fib[i] + fib[i - 1] < 4000000:
    fib.append(fib[i] + fib[i - 1])
    i = i + 1
total = 0
for val in fib:
    if val % 2 == 0:
        total = total + val
print(total)
