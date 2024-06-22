def count(number):
    return len(str(number))

number = int(input("Enter the number: "))
print(f"The length of {number} is {count(number)}")
