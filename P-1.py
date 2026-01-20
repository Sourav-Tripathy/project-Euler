
# Problem link : https://projecteuler.net/problem=1

# problem Statement : Find the sum of all the multiples of 3 or 5 below 1000.

def find_sum ():
  sum = 0
  for i in range(1,1000):
    if i%3 == 0 or i%5 == 0 :
      sum+=i
  return sum

if __name__ == "__main__":
    result = find_sum()
    print(result)