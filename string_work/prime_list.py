def isprime(x):
    for j in range(2, int(x**0.5) + 1):
        if x % j == 0:
            return False

    return True


def next_prime(p):

    while True:
        if p == 2:
            yield 3
        elif isprime(p+2):
            yield p+2
        else:
            p += 2


primes = [0, 2]
n = int(input())
s = [int(i) for i in input().split()]

for i in s:
    while len(primes) <= i:
        primes.append((next(next_prime(primes[-1]))))
    print(primes[i], end=" ")


