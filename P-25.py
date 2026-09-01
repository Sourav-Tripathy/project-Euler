# Problem link : https://projecteuler.net/problem=25
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

def fib():
    f1=1
    f2=1
    count=2
    while True:
        f1,f2=f2,f1+f2
        count=count+1
        if len(str(f2))==1000:
            return count

print(fib())