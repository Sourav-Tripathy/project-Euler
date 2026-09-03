# Problem link : https://projecteuler.net/problem=40

# Champernowne's Constant - Finding the indexth digit when the numbers are written 1 to a given length

# verification code

def get_digit(n):
   s = "".join(str(i) for i in range(1, 100000001))
   return s[n - 1]


# formulaic path

def digit(n):
   s = len(str(n))
   total_traversed = 0
   current_low = 0

   for i in range(1, s + 1):
       low = 10 ** (i - 1)
       high = (10 ** i) - 1
       number_to_traverse_in_that = (high - low + 1) * i

       number_to_travel_from_current_low = n - total_traversed

       if number_to_travel_from_current_low <= number_to_traverse_in_that:
           blocks_to_traverse = number_to_travel_from_current_low // i
           reminder = number_to_travel_from_current_low % i

           current_low = low
           index = (current_low + blocks_to_traverse) - 1
           if reminder == 0:
               indexth_digit = index % 10
           if reminder > 0:
               indexth_number = index + 1
               g = str(indexth_number)
               indexth_digit = g[reminder - 1]
           return indexth_digit

       if number_to_travel_from_current_low > number_to_traverse_in_that:
           total_traversed = total_traversed + number_to_traverse_in_that
           current_low = low

def get_product():
    f=1
    for i in range(0,7):
        d = 10**i
        s=digit(d)
        f = int(f)*int(s)
    return f

if __name__ == "__main__":

    print(get_product())
#    d = 12345678901145
# print(get_digit(d))
# print(f"formula",digit(d))


# The trick is to find in which range the number lies in and then traverse from start to that and then find diff and then traverse the diff from lower count and then traverse that indes and the reminder as per that