num = int(input("Enter the number: "))

def check_palindrome(num):
    num_to_str = str(num)

    if num_to_str == num_to_str[::-1]:
        return True
    else:
        return False
    
if check_palindrome(num):
    print(f'{num} is palindrome')
else:
    print(f"{num} is not palindrome")