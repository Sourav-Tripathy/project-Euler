# Problem link : https://projecteuler.net/problem=2

# problem Statement : sum of fibonnaci numbers upto 4 million contsraint numbers that are even only


def even_fibonacci_sum(limit=4_000_000):
    a, b = 1, 2
    c = 0

    while a <= limit:
        if a % 2 == 0:
            c += a
        a, b = b, a + b

    return c


if __name__ == "__main__":
    print(even_fibonacci_sum())