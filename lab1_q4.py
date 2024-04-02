def reverse_string(s):
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string(s[:-1])

input_string = input("Enter a string: ")
result = reverse_string(input_string)
print("The reverse of the string:", result)
