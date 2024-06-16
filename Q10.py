person = {
    "name": "Sandesh Shrestha",
    "age": 20,
    "college": "Inspiria Knowledge Campus"
}

# Adding a new key-value pair
person["city"] = "siliguri"

# Updating a value
person["age"] = 21

# Deleting a key-value pair
del person["college"]

# Printing the dictionary
print("Dictionary contents:")
for key, value in person.items():
    print(f"{key}: {value}")
