def sum_n(n):
    if n == 0:  # Base case: sum of 0 numbers is 0
        return 0
    return n + sum_n(n - 1)  # Recursive call

# Example usage
n = 5
result = sum_n(n)
print("Sum of first", n, "numbers:", result)
