# Problem link : https://projecteuler.net/problem=6

# problem Statement : Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# from airthmetic progression formula sum and sum of square can be calculated directly and that is used here

def sum_square_diff(n):
  s = n*(n+1)*(2*n +1)//6  # sum of squares
  s1 = n*(n+1)//2    # sum of n natural numbers
  c = (s1*s1) - s
  return c

if __name__ == "__main__":
  
  print(sum_square_diff(100))