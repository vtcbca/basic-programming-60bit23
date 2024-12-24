# Method 5: Using a While Loop
def print_pattern(n):
    i = 1
    while i <= n:
        print('* ' * i)
        i += 1

input_lines = int(input("Enter number of lines: "))  # Input number of lines
print_pattern(input_lines)
