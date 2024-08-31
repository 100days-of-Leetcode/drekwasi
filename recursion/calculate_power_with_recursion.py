"""
Calculate the power of number based using recursion
"""
def power_n(base, exp):
    assert exp >= 0 and int(exp) == exp, "Positive integers only"
    if exp == 0:
        return 1
    return power_n(base, (exp - 1)) * base

print(power_n(0, 6))