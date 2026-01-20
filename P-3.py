# Problem link : https://projecteuler.net/problem=3

# problem Statement : Finding largest prime fasctor of 600851475143 

# done via Brute Force Method

n = 600851475143
d = 2
f = []

while n > 1:
    if n % d == 0:
        f.append(d)
        n //= d
    else:
      d+=1

print(max(f))