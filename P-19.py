# Problem link : https://projecteuler.net/problem=19

# problem Statement : between 1 jan 1901 and 31 dec 2000  find the number of sunday on the first of month

def l_y(y):
   if y%4==0 and y%100!=0 or y%400==0:
       return True
   return False

def d_I_m(m,y):
   if m in [1,3,5,7,8,10,12]:
       return 31
   elif m in [4,6,9,11]:
       return 30
   elif m==2:
       if l_y(y):
           return 29
       else:
           return 28

def d_I_y(y):
   d=0
   for i in range(1900,y):
       if l_y(i):
           d+=366
       else:
           d+=365
   return d

def d_I_m_y(m,y):
   d=d_I_y(y)
   for i in range(1,m):
       d+=d_I_m(i,y)
   return d

def main():
   count=0
   for y in range(1901,2001):
       for m in range(1,13):
           if (d_I_m_y(m,y)+1)%7==0:
               count+=1
   print(count)

if __name__=="__main__":
   main()