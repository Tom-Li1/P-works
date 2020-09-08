from time import clock

def calPrime(n):
    primes = []

    for i in range(3, n + 1, 2):
        max = int(i ** .5)
        for prime in primes:
            if prime > max:
                primes.append(i)
                break
            elif not i % prime:
                break
        else:
            primes.append(i)

    if n >= 2:
        primes.insert(0, 2)

    return primes

c = clock()
primes = calPrime(2000000)
print(clock() - c)
#print primes
print(len(primes), '\n=========================')
print('Answer:', sum(primes))