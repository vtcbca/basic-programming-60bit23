input_string = input("Enter a string: ")
stack = list(input_string)  # Convert string to list (stack)
reversed_string = ""
while stack:
    reversed_string += stack.pop()  # Pop elements from the stack
print("Reversed string:", reversed_string)