def gcd(a, b):
    """
    This function returns the greatest common divisor (GCD) of two numbers using recursion.
    """
    if b == 0:  # Base case
        return a
    else:       # Recursive case
        return gcd(b, a % b)

# Example usage:
print(gcd(48, 18))  # Output: 6