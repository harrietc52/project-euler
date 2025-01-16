# To Run:
# `python3 multiples_of_3_or_5/solution.py`

# Problem:
# If we list all the natural numbers below 10 that are multiples
# of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


def find_multiples_of_3_and_5_below(number):
    result = 0
    multiples = []

    # 3
    i = 1
    while result < number-3:
        result = 3 * i
        multiples.append(result)
        i += 1

    # 5
    j = 1
    result = 0
    while result < number-5:
        result = 5 * j
        multiples.append(result) if result not in multiples else None
        j += 1

    return sorted(multiples)



def test_find_multiples_of_3_and_5_below(number):
    multiples = find_multiples_of_3_and_5_below(number)
    result = sum(multiples)

    expected = 23

    print(result == expected, ": Expected %s, got %s" % (expected, result))


test_find_multiples_of_3_and_5_below(10)
# test_find_multiples_of_3_and_5_below(1000)


