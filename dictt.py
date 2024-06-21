person = {
    "Name": "sandesh",
    "Age": 19,
    "College": "Inspiria Knowledge Campus"
}

person["Name"] = "Sandesh shrestha"
person["Address"] = "Siliguri"
del person["Age"]
print(person)

for key, value in person.items():
    print(f'{key} : {value}')