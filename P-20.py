# Problem link : https://projecteuler.net/problem=20
# Sum of digits of the number which is produced when you find out 100 fatctorial

def sum(n):
    s= 1
    for i in range(1,n+1):
        s=s*i
    # print(s)

    s = str(s)
    m=0
    for i in range(0,len(s)):
        m = m + int(s[i])
    return m


print(sum(100))