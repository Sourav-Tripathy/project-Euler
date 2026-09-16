# Problem link : https://projecteuler.net/problem=30
#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.


import sys

def find_numbers(n,k):
    m=str(n)
    g=[]
    for i in m:
        g.append(int(i))

    su=0
    for i in g:
        su+=pow(i,k)
    
    if su==n:
        return True
    return False


def find_limit_to_search(n):
    max = 9**n
    d=1
    while 10**(d-1)<=d*(max):
        d+=1
        print(d)

    return 10**(d-1)


def find_numbers_and_sum(n):
    l=[]
    g=find_limit_to_search(n)
    for i in range(2,g+1):
        if find_numbers(i,n):
            l.append(i)
            print(l)
    su=0
    for j in l:
        su+=j
    return su

print(find_numbers_and_sum(5))
# print(find_limit_to_search(4))



# Note: A d-digit number must be at least 10**(d-1),while the maximum possible sum of its digits raised to the nth power is d * 9**n.Once 10**(d-1) > d * 9**n, no d-digit number can satisfy the condition.
