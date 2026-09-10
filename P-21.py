# Problem link : https://projecteuler.net/problem=21

# Evaluate the sum of all amicable numbers under 10000 . (Amicable numbers are those whose divisors add up to so,e number and then when we take that some number and find its divisors and add then the first number pops up...then those two numbers are amicable numbers...ex 284 and 220) pairs can not be equal

# Done via brute force

def find_all_divisors_then_sum(n):
    f = []
    sum_f = 0
    for i in range (1,n):
        if n%i == 0:
            f.append(i)
            i+=1
        else:
            i+=1
    for j in f:
        sum_f=sum_f+j
    # print(f)
    # print(sum_f)
    return sum_f

# find_all_divisors_then_sum(284)

def find_amicable_pairs(a):
    amicable_pairs=[]
    pair_sums=[]
    for i in range(1,a):
        s=find_all_divisors_then_sum(i)
        m=find_all_divisors_then_sum(s)
        if m==i and i!=s:
            h=i+s
            if h not in pair_sums:
                amicable_pairs.append([i,s])
                pair_sums.append(h)
        else:
            i+=1
    print(amicable_pairs)
    print(pair_sums)
    pair_total=0
    for i in pair_sums:
        pair_total=pair_total+i
    print(pair_total)
    return amicable_pairs,pair_sums

find_amicable_pairs(10000)