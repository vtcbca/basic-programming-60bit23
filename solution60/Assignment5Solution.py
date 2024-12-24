# Method 5: Using a Stack (List)
def is_palindrome(s):
    s = s.replace(" ", "").lower()  # Remove spaces and make lowercase
    stack = list(s)  # Convert string to stack
    reversed_s = ""
    while stack:
        reversed_s += stack.pop()  # Pop elements to reverse the string
    return s == reversed_s

input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
