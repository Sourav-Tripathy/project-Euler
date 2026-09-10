#Problem link : https://projecteuler.net/problem=27
# we have an equation n^2+an+b , where a is in range -1000 to 1000 (non inclusive) and b is in range -1000 to 1000 (inclusive). the vlaue of n will lie in between 0 to a (inclusive) such that in that range of n values any integer n vlaue will give us primes....so we have to find the value of a,b such that we get max primes

# for n=0, result is b , so b must be always prime there for search space of b should be a prime in between 0 to 1000

def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

# print(check_prime(21))

list_b = []
for i in range (2,1001): 
    if check_prime(i):
        list_b.append(i)

# print(list_b)

            
def find_coeff():
    max_primes = 0
    best_a, best_b = 0, 0
    for a in range(-999, 1000):
        for b in list_b:
            n=0
            while True:
                s = n*n + a*n + b
                if not check_prime(int(s)):
                    break
                n +=1     
            if n > max_primes:
                max_primes = n
                best_a, best_b = a, b
    print(best_a*best_b)
    return best_a, best_b, max_primes

print(find_coeff())