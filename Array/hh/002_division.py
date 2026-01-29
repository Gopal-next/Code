def division(a, b):
    if b == 0:
        return "Error: Division by zero is undefined."
    return a / b
print(division(10, 2))  # Output: 5.0
print(division(7, 0))   # Output: Error: Division by zero is undefined.