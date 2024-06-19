Heroes = ["superman", "batman", "spiderman", "Ironman"]

for item in Heroes:
    if(item == "spiderman"):
        continue
    print(item)

for item in Heroes:
    if(item == "spiderman"):
        break
    print(item)