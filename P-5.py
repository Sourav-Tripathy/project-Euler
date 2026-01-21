# Problem link : https://projecteuler.net/problem=5

# problem Statement : What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 ?

# LCM is the smallest number divisible by each number so lcm fiding does the task

def gr_c_d(a,b):
  while b:
    a,b = b ,a%b
  return a
def lr_cm(a,b):
  s = (a*b)//gr_c_d(a,b)
  return s
c=1
for i in range(1,21):
  c = lr_cm(c,i)

print(c)