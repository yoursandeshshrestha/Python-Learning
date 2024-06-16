def is_armstrong(num):
    # Convert number to string to iterate over each digit
    num_str = str(num)
    
    # Calculate the number of digits
    num_digits = len(num_str)
    
    # Calculate sum of digits each raised to the power of num_digits
    sum = 0
    for digit in num_str:
        sum += int(digit) ** num_digits
    
    # Check if the sum equals the original number
    return sum == num

# Example usage:
num = 153
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
