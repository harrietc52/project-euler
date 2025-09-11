# Problem 3
# The prime factors of 13195 are 5,7,13 and 29.

# What is the largest prime factor of the number 600851475143?
# To run: `python3 largest_prime_factor/solution.py`

# Calculating for 13195 works, however calculating for the requested 600851475143
# is too computationally heavy, and times out.

NUMBER = 13195 # Prime Factors are [5, 7, 13, 29]
# NUMBER = 600851475143

# Prime numbers are only divisible by 1 and itself
def calculate_prime_numbers(highest_number):

    # Start with a list of numbers up to a certain limit.
    list_of_possible_prime_numbers = list(range(2, highest_number+1))

    # Eliminate multiples of each prime number
    for item in list_of_possible_prime_numbers:
        for x in list_of_possible_prime_numbers:
            result = x/ item
            divisibe_by_two = (result == int(result))
            if (divisibe_by_two):
                if x != item:
                    list_of_possible_prime_numbers.remove(x)

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


def largest_prime_factor():
    # Divide number by 2, to get number to calculate prime numbers to up
    highest_number = int(NUMBER / 2)

    prime_numbers = calculate_prime_numbers(highest_number)

    prime_factors_list = find_prime_factors(prime_numbers)
    print(prime_factors_list)


largest_prime_factor()
