def sum_digits(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n //= 10
    return total
def max_digit(n):
    maximum = 0
    while n > 0:
        digit = n % 10
        if digit > maximum:
            maximum = digit
        n //= 10
    return maximum
def min_digit(n):
    minimum = 9
    while n > 0:
        digit = n % 10
        if digit < minimum:
            minimum = digit
        n //= 10
    return minimum