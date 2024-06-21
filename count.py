def count_alphanumeric(input_string):
    count = 0
    for char in input_string:
        if char.isalnum():
            count += 1
    return count

# Example usage
user_input = input("Enter a string: ")
alphanumeric_count = count_alphanumeric(user_input)
print(f"The number of alphanumeric characters in the string is: {alphanumeric_count}")
