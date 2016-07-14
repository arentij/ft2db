def is_prime(x):
    for j in range(2, int(x**0.5) + 1):
        if x % j == 0:
            return False
    return True


def gen_primes():
    n = 2
    primes = set()
    while True:
        for p in primes:
            if n % p == 0:
                break
        else:
            primes.add(n)
            yield n
        n += 1

primes = gen_primes()
print(next(primes))
print(next(primes))
print(next(primes))
