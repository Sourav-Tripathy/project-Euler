# Problem link : https://projecteuler.net/problem=15
# if we have a m*m grid , we have to find unique path to reach from top left to bottom right corner while moving right and down (these two freedom of movement exists) its always a square matrix

# The trick is any path we choose we have to take m right steps and m down steps always that means total 2m steps we have to take that means it becomes an combinatorics problem where total paths will be 2mcm.


def factorial(n):
    if n ==0:
        return 1
    else:
        return n*factorial(n-1)


def grid_size(n):
    s=factorial(2*n)/(factorial(n)*factorial(n))

    return s

print(grid_size(20))
    
