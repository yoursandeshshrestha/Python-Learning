string = input("Enter a string: ")

print(f"Length of the string: {len(string)}")
print(f"Uppercase: {string.upper()}")
print(f"Lowercase: {string.lower()}")
print(f"Reversed: {string[::-1]}")
if string == string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
