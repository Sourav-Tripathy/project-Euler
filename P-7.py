# Problem link : https://projecteuler.net/problem=7

# problem Statement : What is the  10001 st prime number?
# by prime number theorem pth prime is approximately p(lnp+lnlnp)so this is the upper and then we use sieve method to find all prime up to that and inside a list and we take our index 

import math
import numpy as np

p = 10001

a_p = np.round( p*(math.log(p)+math.log(math.log(p))))
s = int(a_p)

def all_p(n):
    is_p = [True] * (n + 1)
    is_p[0] = is_p[1] = False

    i = 2
    while i * i <= n:
        if is_p[i]:
            for x in range(i*i, n+1, i):
                is_p[x] = False
        i += 1

    return [i for i in range(2, n+1) if is_p[i]]
m = all_p(s)
print(m[p-1])