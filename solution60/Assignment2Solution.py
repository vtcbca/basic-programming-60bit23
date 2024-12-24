def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers
    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return primes

def is_prime_sieve(n):
    if n <= 1:
        return False
    primes = sieve_of_eratosthenes(n)
    return primes[n]

# Test the function
number = int(input("Enter a number: "))
if is_prime_sieve(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")