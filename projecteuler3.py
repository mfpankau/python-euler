factors = [1]
def findFactor(num):
    global factors
    for i in range(2, num + 1):
        if num % i == 0:
            factors.append(i)
            print('found factor: ' + str(i))
            return int(num / i)

def main(num):
    x = num
    while x != 1:
        x = findFactor(x)
    print('largest prime factor: ' + str(factors[len(factors) - 1]))

if __name__ == '__main__':
    main(600851475143)
