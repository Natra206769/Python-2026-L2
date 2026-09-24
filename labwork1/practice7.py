s = input("Enter the string: ")

def remove_dollar_sign(s):
    new_string = ""
    for i in range(1, len(s)):
        if s[i] != "$":
            new_string += s[i]
    return new_string

print(remove_dollar_sign(s)) 