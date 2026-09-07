# Problem link : https://projecteuler.net/problem=12
# we are trying to find the smallest traingle number which has minimum 500 divisors


def find_triangle_number(n):
    s=n*(n+1)//2
    return s

# print(find_triangle_number(7))


def find_count(n):
    f=[]
    d = 2
    while n > 1:
        if n % d == 0:
            f.append(d)
            n //= d
        else:
            d+=1
    unique_power=[]
    g=set(f)
    for i in g:
        count=f.count(i)
        unique_power.append(count+1)
    # print(unique_power)
    l=1
    for i in unique_power:
        l=l*i

    return l


def find_number():
    s=0
    i=1
    while s<=500:
        m=find_triangle_number(i)
        s = find_count(m)
        i=i+1
        print(f"{s} divisors of {m}")
    return s,m
    
print(find_number())


# Note: While finding the number of divisors of a number what we do is we find out the prime factors of the number in concern and then make a list of them(they can be repeated) and then we write them each uniques power and then take each power plus 1 and then multiply
        
