# Problem link : https://projecteuler.net/problem=34
# Find the sum of all numbers which are equal to the sum of the factorial of their digits. except 1 and 2

def calc_factorial(n):
   if n==0:
       return 1
   else:
       return n*calc_factorial(n-1)


def check_number(n):
   g=str(n)
   sum=0
   for i in g:
       sum+=calc_factorial(int(i))
   if sum==n:
       return True
   return False

def sum_all_true_check_number():
   sum=0
   # g=[]
   for i in range (3,9999999):
       if check_number(i):
           sum+=i
           # g.append(i)
   return sum

print(sum_all_true_check_number())
# print(check_number(346))


# Note - if we take 9999999 here 7 times 9! exceeds 9999999 and hence that here taken as the upper limit