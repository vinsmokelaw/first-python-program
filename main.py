# passcode = input ("enter passcode: ")
# while passcode == "":
#     print("error")
#     passcode = input ("enter passcode: ")
# else:
#    print(f"{passcode} is correct")
# weight = input("Step on scale:  ")
# while weight > "150":
#   print("You are over weight")
#   weight = input("Step on scale:  ")
# else:
#   print(f"{weight} is normal")   
# cats = 10
# dogs = cats >= 6
# catsAndDogs = dogs and cats < 15
# print(catsAndDogs)
# apples = 12
# oranges = 8
# peaches = apples and oranges >= 15
# apples_oranges_peaches = apples and oranges and peaches < 20
# print(apples_oranges_peaches)
# isHuman = True
# isAlien = False
# result = isAlien or isHuman
# print(result)
# isWarm = False
# isCold = True
# result = isWarm or isCold
# print(result)
# isHuman = False
# result = not isHuman
# print(result)
# speed = 12
# isFast = speed >= 7
# isAtheletic = True
# result = isFast and (isAtheletic or speed < 10)
# print(result)
# price = 30
# colour = "white"
# isCorrctPrice = price == 30
# isCorrctColour = colour == "white"
# results = isCorrctPrice and isCorrctColour
# print(results)
# apples = {"red", "green", "yellow", "blue", "purple", "orange", "pink", "black", "white", "grey"}

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print(f"Hello {name}, you are {age} years old.")

# a = 30
# b = 20
# c =10
# print( a > b and b == c)   
# print( a > b or b == c)
# print( a > b and not b == c)
# print( a > b or not b == c)
# print( a > b and c == a)
# print( a > b or c == a)
# print( a > b and c != a)

# username = "Tawanda"
# password = 1234
# age = 18
# username = input("Enter username: ")
# password = int(input("Enter password: "))
# age = int(input("Enter age: "))        
# if username == "Tawanda" and password == 1234 and age >= 20:
#    print(f"Welcome {username}, you are {age} years old and your password is {password}.")
# else:
#    print("Access denied")

# temparature = int(input("Enter the tempature: "))
# sunny = input("Is it sunny? (yes/no): ").lower()
# cold = input("Is it cold? (yes/no): ").lower()
# temparature = 30
# condition = (sunny == "yes" and temparature >= 30) or  (cold == "yes" and temparature < 20)
# if sunny == "yes" and temparature >= 30:
#    print(f"It's a sunny day, wear shorts.")
# else:
#    print(f"It's not cold day, wear long pants.") 

# day = input("Enter Day: ").lower()   
# if day == "monday":
#    print("wear uniform")
# elif day == "tuesday":
#    print("wear garments")
# elif day == "wednesday":
#    print("wear shorts")
# elif day == "thursday":
#    print("wear jeans")
# elif day == "friday":
#    print("wear t-shirt")
# elif day == "saturday":
#    print("wear hoodie")
# elif day == "sunday":
#    print("wear jacket")

# days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
# day = input("Enter Day: ").lower()  
# if day in days:
#    print(f"{day} is a valid day.")
# else:
#    print(f"{day} is not a valid day.")

# grade = int(input("Enter your grade: "))
# grades = ["A", "B", "C", "D", "F"]
# if grade >= 90:
#    print("You got an A")
# elif grade >= 80:
#    print("You got a B")
# elif grade >= 70:
#    print("You got a C")
# elif grade >= 60:
#    print("You got a D")
# else:
#    print("You got an F")

# student = { 
#    "name": "Tawanda",
#    "age": 18,}
# student["age"] = 30    
# print(student)
# student.update({"country": "Zimbabwe", "city": "Harare"})
# print(student)
# student.update({"cell": 123456789, "address": "123 Main St"})
# print(student)
# student.clear()
# print(student)

# students = ("Tawanda", "Tinashe", "Tafadzwa", "Tendai", "Tafara", "Tinashe", "Tafadzwa", "Tendai", "Tafara")
# print(students[1:-1:5])

# firstName = "Tawanda"
# food = "Burger"
# print(f"hello {firstName} you like {food}")



# list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(type(list2))

# fruits = {1, 1,  2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
# fruits1 = {2, 3, 4, 5, 6}
# union_set = fruits | fruits1 
# print(help(fruits))
# print(union_set )

# name = input("Enter your name: ")
# while name == "":
#     print("Error")
#     name = input("Enter your name: ") 

# i = 0
# while i >  10:
#     print(i)
#     i += 1 
# print("Done")

# correct_number = 7
# guess = int(input("Guess a number : "))
# while guess != correct_number:
#      print("Sorry thats not correct try again")
#      guess = int(input("Guess a number : "))
# print("You win")

# correctNumber = 7
# guess = int(input("Guess a number : "))
# while True :
#     if guess > correctNumber:
#         print("You win")
#         guess = int(input("Guess a number : "))
#     elif guess < correctNumber:
#         print("Too low")
#         guess = int(input("Guess a number : "))
#     else:
#         print("Too high")
#     guess = int(input("Guess a number : "))
# print("You win")

# carStarted = False
# while True:
#     command = input("Enter command (start/stop/quit/help): ").lower ()
#     if command == "start":
#         if carStarted == True:
#             print("Car already started.")
#         else:
#             carStarted = True
#             print("car started.")
#     elif command == 'help':
#         print("""
#         start - to start the car
#         stop - to stop the car
#         quit - to quit
#         """)
#     elif command == "stop":
#         if carStarted:
#             carStarted = False
#             print("car stopped.")
#         else:
#             print("car already stopped.")
#     elif command == "quit":
#         print("Exiting program.")
#         break  # Exits the loop
#     else:
#         print("Invalid command. Use start, stop, or quit.")

# carStarted = False
# while True:
#     command = input("Enter command (start/stop/quit): ")
#     if command == "start":
#         running = True
#         print("Process started🤩.")
#     elif command == "stop":
#         running = False
#         print("Process stopped✔.")
#     elif command == "quit":
#         print("Exiting program😢.")
#         break
#     elif command == 'help':
#         print("""
#         start - to start the car
#         stop - to stop the car
#         quit - to quit
#         """)
#     else:
#         print("Invalid command.")

# i = 0
# while i <= 20:
#     print(i)
#     i += 2  # Decrement i by 1
# print("Liftoff!")    





