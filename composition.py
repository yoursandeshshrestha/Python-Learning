def mul(num):
    return num * 2

def add(num):
    return num + 2

def round(num):
    return mul(add(num))

num = int(input("Enter the number: "))
result = round(num)
print(f"The result will be {result}")