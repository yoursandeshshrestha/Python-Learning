# Working with a list
numbers = list(map(float, input("Enter numbers separated by space: ").split()))

largest = max(numbers)
smallest = min(numbers)

print(f"Largest number in the list is {largest}")
print(f"Smallest number in the list is {smallest}")

# Working with a tuple
numbers_tuple = tuple(numbers)
print(f"Largest number in the tuple is {max(numbers_tuple)}")
print(f"Smallest number in the tuple is {min(numbers_tuple)}")
