# Problem link : https://projecteuler.net/problem=24
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# possible of 012 is 012, 021, 102, 120, 201, 210 

# brute force using itertools library

import itertools

m=[0,1,2,3,4,5,6,7,8,9]

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

def arrange_lexographic(l):
    l=sorted(l)
    n=len(l)
    s=list(itertools.permutations(l))
    return s


g=arrange_lexographic(m)
h=list(g[1000000-1])

f="".join(str(i) for i in h)

print(f)