"""
Find the sum of digits of a positive integer using recursion
"""

def sum_digits(n):
    assert n >= 0 and int(n) == n, "Positive integers only"
    if n == 0:
        return 0
    else:
        return sum_digits(n // 10) + (n % 10)

print(sum_digits(123553243))