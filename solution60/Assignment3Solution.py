def fibonacci_list_comprehension(max_value):
    fib_sequence = [0, 1]
    while fib_sequence[-1] + fib_sequence[-2] <= max_value:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Test the function
max_val = int(input("Enter the maximum value: "))
print(f"Fibonacci sequence (up to {max_val}): {fibonacci_list_comprehension(max_val)}")
