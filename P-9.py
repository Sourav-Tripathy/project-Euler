# Problem link : https://projecteuler.net/problem=9

# problem Statement : find abc where a<b<c and a+b+c =1000 and a,b,c are pyhtogorian triplet i.e a^2+b^2 = c^2 .


s = []
p = 0
for a in range (1,1000):
  for b in range(a+1,1000):
    c = 1000-a-b
    if c > b :
      if a*a +b*b == c*c:
        p+= a*b*c
        s.append(a)
        s.append(b)
        s.append(c)
print(s)
print(p)