def string_to_integer(s):
    s = s.replace(',', '')
    integer_value = int(s)
    s = str(integer_value)
    
    length = len(s)
    if length <= 3:
        return s
    elif length <= 5:
        return s[:-3] + ',' + s[-3:]
    else:
        return s[:-5] + ',' + s[-5:-3] + ',' + s[-3:]

input_string = input("Enter a string of digits: ")
result = string_to_integer(input_string)
print("The integer representation of the entered string is:", result)
