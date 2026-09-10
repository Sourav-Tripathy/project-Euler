# Problem link : https://projecteuler.net/problem=37
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

def check_prime(n):
    if n<=1:
        return False
    for i in range(2,(int(n**0.5))+1):
        if n%i==0:
            return False
    return True

def all_truncatable(n):
    s=str(n)
    g=[]
    for i in s:
        g.append(i)
    h=g.copy()
    all=[]
    all.append(n)
    for i in range(0,len(h)-1):
        h.pop(-1)
        m="".join(j for j in h)
        all.append(int(m))

    for i in range(0,len(g)-1):
        g.pop(0)
        k="".join(j for j in g)
        if int(k) not in all:
            all.append(int(k))
    return all
            
        
def find_truncate_prime():
    max=11
    count=0
    truncate_primes=[]
    h=11
    while True:
        i=h
        if count<max:
            all=all_truncatable(i)
            m=0
            for j in all:
                if check_prime(j):
                    m+=1
            if m==len(all):
                truncate_primes.append(i)
                count+=1
                # print(truncate_primes)
            h+=2
        else:
            break
    
    sum=0
    for j in truncate_primes:
        sum=sum+j

    return truncate_primes,sum




# print(all_truncatable(3797))
print(find_truncate_prime())