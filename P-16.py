# Problem link : https://projecteuler.net/problem=16

# sum of digits of 2 to the power 1000

s = pow(2,1000)
sum=0
for i in str(s):
    sum=sum+int(i)

print(sum)