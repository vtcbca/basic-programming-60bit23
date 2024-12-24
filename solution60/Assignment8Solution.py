# Method 5: Using While Loop
def print_pattern(n):
    i = 1
    while i <= n:
        # Print leading spaces
        print(' ' * (n - i), end='')
        
        # Print increasing characters
        j = 1
        while j <= i:
            print(chr(64 + j), end=' ')
            j += 1
        
        # Print decreasing characters
        j = i - 1
        while j >= 1:
            print(chr(64 + j), end=' ')
            j -= 1
        
        print()  # Move to the next line
        i += 1

input_lines = int(input("Enter the number of lines: "))  # Input number of rows
print_pattern(input_lines)
