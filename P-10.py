# Problem link : https://projecteuler.net/problem=10

# problem Statement : Find the sum of all the primes below two million.

def si(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= n:
        if is_prime[p]:
            for multiple in range(p*p, n+1, p):
                is_prime[multiple] = False
        p += 1

    return [i for i in range(2, n+1) if is_prime[i]]

m = si(2000000)
s = 0
for i in m:
  s+=i

print(s)