# Problem link : https://projecteuler.net/problem=4

# problem Statement : Find the largest palindrome made from the product of two 3-digit numbers.

m = []
for i in range(100,1000):
  for j in range(i+1,1000):
    m.append(i*j)

# print(len(m))

h = []

for a in m:
  if str(a) == str(a)[::-1]:
    h.append(a)


print(max(h))