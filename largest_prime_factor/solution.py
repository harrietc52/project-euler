# Problem 3
# The prime factors of 13195 are 5,7,13 and 29.

# What is the largest prime factor of the number 600851475143?
# To run: `python3 largest_prime_factor/solution.py`

# Calculating for 13195 works, however calculating for the requested 600851475143
# is too computationally heavy, and times out.

# NUMBER = 35
NUMBER = 13195 # Prime Factors are [5, 7, 13, 29]
# NUMBER = 600851475143

# Prime numbers are only divisible by 1 and itself
def calculate_prime_numbers(highest_number):

    list_of_possible_prime_numbers = []

    if highest_number >= 2:
        list_of_possible_prime_numbers.append(2)

    for item in range(3, highest_number+1):
        if item % 2 == 0:
            continue

        for x in range(3, item):
            is_x_a_factor = (item % x == 0)

            if (is_x_a_factor):
                if x not in list_of_possible_prime_numbers:
                    list_of_possible_prime_numbers.append(x)

    return list_of_possible_prime_numbers


def find_prime_factors(prime_numbers):
    prime_factors = []

    result = NUMBER

    for prime_number in prime_numbers:
        # Divide the number by each prime number, starting from the smallest,
        # as many times as possible, until the result is not a whole number
        while (result / prime_number == int(result / prime_number)):
            prime_factors.append(prime_number)
            result = result / prime_number

    return prime_factors


def calculate_square_root():
    # ** is to the power of
    sqareroot = int(NUMBER**0.5)
    return sqareroot


def largest_prime_factor():
    highest_number = calculate_square_root()

    prime_numbers = calculate_prime_numbers(highest_number)

    prime_factors_list = find_prime_factors(prime_numbers)

    print(prime_factors_list)


largest_prime_factor()
