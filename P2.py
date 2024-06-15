# movie1 = input("Enter the first movie : ")
# movie2 = input("Enter the Second movie : ")
# movie3 = input("Enter the Third movie : ")

# list = []
# list.append(movie1)
# list.append(movie2)
# list.append(movie3)
# print(list)

Test = input("Enter something : ")

Test_copy = Test[::-1]

if(Test == Test_copy):
    print("Palindrome")
else:
    print("Not Palindrome")

