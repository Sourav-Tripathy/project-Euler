# Problem link : https://projecteuler.net/problem=35

# 197 is a circular prime i.e 197,971,719 are all primes. because all rotations are prime.
# we have to find how many such exists below 1 million.

# note: we are only checking odds and also removing those odd numbers in which an even digit exists and also we are directly adding all rotations of circular prime to avoid double checking

def check_prime(n):
    if n<=1:
        return False
    for i in range(2,(int(n**0.5))+1):
        if n%i==0:
            return False
    return True

def single_rotation(n):
    f=[]
    g=[]
    s=str(n)
    for i in s:
        g.append(i)
    # print(g)
    h=g.pop(-1)
    # print(h)
    new_g=h+"".join(i for i in g)

    return new_g
 
# print(single_rotation(123))


def return_all_rotations(n):
    all_rotations=[]
    all_rotations.append(n)
    for i in range(1,len(str(n))):
        m=single_rotation(n)
        all_rotations.append(int(m))
        n=m
    return all_rotations

def all_digit_odd(n):
    s=str(n)
    g=[]
    for i in s:
        g.append(int(i))
    if 5 in g:
        return False
    m=0
    for i in g:
        if i%2!=0:
            m=m+1
    if m==len(s):
        return True
    return False



def find_circular_prime_in_range(n):
    circular_primes=[2,5,11]
    h=[]
    for i in range(3,n+1,2):
        if i not in circular_primes:
            if all_digit_odd(i):
                f=return_all_rotations(i)
                m=0
                for x in f:
                    if check_prime(x):
                        m=m+1
                if m==len(f):
                    for j in f:
                        circular_primes.append(j)
        else:
            h.append(i)
            # print(i)
    
    return len(circular_primes),circular_primes



print(find_circular_prime_in_range(1000000))