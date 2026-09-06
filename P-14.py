# Problem link : https://projecteuler.net/problem=14

# Collatz Sequence - Basically taken two laws and if started from a number it always reaches to 1 at the end as the chain goes...Its an unsloved problem of mathematics
# here rules are if n even n/2 , if odd 3n+1 and the chain goes on

# Which starting number, under one million, produces the longest chain ?

# done via brute force


def build_chain(n):
    f=[]
    s=[]
    f.append(n)
    while n!=1:
        if n%2==0:
            n = n//2
            f.append(n)
        else:
            n = 3*n+1
            f.append(n)
    m=len(f)
    s.append([f[0],m])
    # print(f)
    # print(s)
    return f,s

# build_chain(4)

def build_chain_for_range(n):
    g=[]
    for i in range(1,n):
        l,m=build_chain(i)
        g.append(m[0])

    # print(g)
    max_pair = max(g, key=lambda x: x[1])
    print (max_pair)
    return g,max_pair

build_chain_for_range(1000000)
