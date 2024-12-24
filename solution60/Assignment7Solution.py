# Method 5: Using a While Loop
def print_triangle(n):
    i = 1
    while i <= n:
        # Print spaces
        print(' ' * (n - i), end='')
        # Print numbers
        j = 1
        while j < 2 * i:
            print(j, end=' ')
            j += 1
        print()  # Move to next line
        i += 1

input_lines = int(input("Enter the number of rows: "))  # Input number of rows
print_triangle(input_lines)
