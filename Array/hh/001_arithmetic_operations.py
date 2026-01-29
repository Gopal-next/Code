def arithmetic_operations(a,b):
    return {
        "sum": a + b,
        "difference": a - b,
        "product": a * b,
        "quotient": a / b if b != 0 else float('inf')
    }
print(arithmetic_operations(10, 5))
print(arithmetic_operations(7.5, 2.5))