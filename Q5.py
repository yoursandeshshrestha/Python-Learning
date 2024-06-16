
num = int(input("Enter the number: "))

def is_palindrome(num):
    # Convert number to string to easily check palindrome
    num_str = str(num)
    
    # Check if the number string is equal to its reverse
    if num_str == num_str[::-1]:
        return True
    else:
        return False

if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")



