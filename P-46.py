# Problem link : https://projecteuler.net/problem=46

# Odd composite number can be expressed as the sum of prime and twice of a square, find smallest which defies this property


import math

def is_odd_composite(n):
    if n % 2 == 0 or n < 9:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return True
    return False


# print(is_odd_composite(9946))

def is_prime(a):
    if a < 2:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True

# # print(is_prime(4877))

def is_perfect_square(n):
    if n < 0:
        return False
    a = int(math.sqrt(n))
    if a*a == n:
        return True
    return False


for i in range(2,10000):
    if is_odd_composite(i):
        sat=False
        for j in range(2,i):
            if is_prime(j):
                k = (i-j)/2
                if k>0 and is_perfect_square(k):
                    # print("ok",i)
                    sat=True
                    break
        if not sat:
            print("not ok",i)

