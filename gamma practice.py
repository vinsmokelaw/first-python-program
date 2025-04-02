# variables = empty containers that stores data
#             behaves as if it was the value it contains
#              (strings, intergers, floats, boolean)

# strings(str)
firstName = "Tawanda"
secondName = "Muchenu"
address = "8471 Budiriro 5B"
language = "Shona, English, Japanese"
eyes = "brown"
food = "pizza"
pet = "Spike"
school = "Uncommon.org"
bFriend = "James"
phone = "Samsung A03s"

print(f"Hello my name is {firstName} {secondName} I live at {address}, i speak {language}.My friend is {bFriend} I attend school at {school}. I like {food}, my eye colour is {eyes}. I have a dog called {pet} and i use a {phone}  ")
print(firstName)
print(secondName)
print(address)
print(language)
print(eyes)
print(food)
print(pet)
print(school)
print(bFriend)
print(phone)

# integers(int)
age = 21
numOfStudents = 39
friends = 2
medals = 5
goals = 30
highscore = 5
weight = 10
batteryPecentage = 66
mark = 90
days = 2

print(f"you are {age} years old and you have {friends} friends")
print(age)
print(numOfStudents)
print(friends)
print(medals)
print(goals)
print(highscore)
print(weight)
print(batteryPecentage)
print(mark)
print(days)

# floats
weight = 13.3
height = 5.11
length = 6.4
distance = 5.7
speed = 9.7
time = 13.50
price = 1.39
voltage = 240.0
version = 13.1
gpa = 4.5

print(weight)
print(height)
print(length)
print(distance)
print(speed)
print(time)
print(price)
print(voltage)
print(version)
print(gpa)
print(f"you are {height} feet tall")

# booleans
isStudent = True
isDrunk = False
Taken = True
Male = True
isHuman = True
likesCats = False
hasDog = True
hasKids = False
allergies = True
canSwim = False
hasTattoos = False

if isStudent:
   print("You are a Student")
else:
   print("You are not a Student")

if isDrunk:
   print("You are Drunk")
else:
   print("You are Sober")   

if Taken:
   print("in a relationship")
else:
   print("Single")

if Male:
   print("You are a Boy")
else:
   print("You are a Girl")

if isHuman:
   print("You are from Earth")
else:
   print("You are from OuterSpace")

if likesCats:
   print("You are a cat person")
else:
   print("You are a dog person")

if hasDog:
   print("You are a dog person")
else:
   print("You are a cat person")

if hasKids:
   print("You are a Father")
else:
   print("You are not a Father") 

if hasTattoos:
   print("You are inked")
else:
   print("You are not inked")

if canSwim:
   print("You are can go in the pool")
else:
   print("You are not allowed in the pool")

if allergies:
   print("You are a allergic")
else:
   print("You are not allergic") 

# type casting : is the process of changing data types to other data types
# string to integer conversion examples:
print(int("100"))  

print(int("-50"))  

print(int(" 42 ")) 

print(int("007"))  

numbers = ["1", "2", "3"]
int_numbers = [int(n) for n in numbers]
print(int_numbers)  

print(int("101", 2))  

print(int("12", 8))  

print(int("A", 16))  

num = int("30")
print(num + 10)  

# float to integer conversion (removes decimal part)
print(int(3.99))  

print(int(-4.8))  

print(int(0.0)) 

print(int(12345.6789)) 

num = int(99.99)
print(num + 1)  

print(int(1.2e3))  

print(int(10 / 3)) 

print(int(float("45.6")))  

float_list = [2.7, 3.9, 5.1]
int_list = [int(x) for x in float_list]
print(int_list) 

# boolean to float conversion examples:
print(float(True))  

print(float(False))  

print(float(True) + 2.5)  

print(float(False) * 10) 

x = float(True)
print(x) 

bool_list = [True, False, True, False]
float_list = [float(b) for b in bool_list]
print(float_list)  

result = float(True) / 2
print(result)  

print(float(True) > 0.5) 

def multiply_by_two(n):
    return n * 2
print(multiply_by_two(float(False)))
print(multiply_by_two(float(True)))   

print(float(5 > 3)) 
print(float(2 > 10)) 

#integers to floats
print(float(5))  

print(float(-10))  

print(float(0))  

print(float(1000000)) 

num = float(8)
print(num + 2.5) 

print(float(5 * 2)) 

int_list = [1, 2, 3, 4]
float_list = [float(x) for x in int_list]
print(float_list)  

print(float("99"))  

print(float(True))  
print(float(False)) 

print(float("inf"))  
print(float("-inf")) 

# intergers to bools
# all convertions are True unless its 0

# # lists
# you can append lists using the .append method
# you can remove from lists using the .remove method
#lists are changable you can have copies in a list ordered as well
names = ["Tawanda", "Tatenda", "Angeline", "Stella", "Tafadzwa",]
fruits = ["apple", "cherry", "watemelon", "peach", "guava"]
grades = [10, 20, 59, 40, 36, 22]
countrys = ["Alabasta", "Dressrossa", "Elbaf", "Skypia",]
numOfStudentsInClass = [39, 40, 30, 49,29]
beta = ["apple", "cherry", "watemelon", 39, 40, 30, "Alabasta", "Dressrossa", "Elbaf",]
delta = ["whatsapp", "instagram" , 500 , True, 0.003]
omega = ["superman", "batman", "wonderwoman", "cyborg", "greenarroew", "flash"]
gamma = [True, "aquaman", "goku" ]
alpha = [0.00, 300, 400, 1.22]

fruits[2] = "coconut"
print(fruits)
names[3] = "Faith"
print(names)
grades[-2] = 20
print(grades)
countrys[-3] = "Wano"
print(countrys)
numOfStudentsInClass[2] = 45
print(numOfStudentsInClass)
beta[6] = "coconut"
print(beta)
gamma[4] = "alpha"
print(gamma)
omega[2] = "coconut"
print(omega)
delta[2] = "coconut"
print(delta)
alpha[2] = "coconut"
print(alpha)

print(grades[0:-1])
print(names[2:4])
print(fruits[0:3])
print(countrys[1:-1])
print(numOfStudentsInClass[::-1])
print(gamma[2:4])
print(delta[2:4])
print(gamma[2:4])
print(omega[2:4])
print(alpha[2:4])

#sets
#unchangeble
#you can add and remove
# no duplictaes allowed
# unordered
names = {"Tawanda", "Tatenda", "Angeline", "Stella", "Tafadzwa"}
fruits = {"apple", "cherry", "watemelon", "peach", "guava"}
grades = {10, 20, 59, 40, 36, 22}
countrys = {"Alabasta", "Dressrossa", "Elbaf", "Skypia"}
numOfStudentsInClass = {39, 40, 30, 49,29}
beta = {"apple", "cherry", "watemelon", 39, 40, 30, "Alabasta", "Dressrossa", "Elbaf"}
delta = {"whatsapp", "instagram" , 500 , True, 0.003}
omega = {"superman", "batman", "wonderwoman", "cyborg", "greenarroew", "flash"}
gamma = {True, "aquaman", "goku"}
alpha = {0.00, 300, 400, 1.22}

print(grades)
print(names)
print(fruits)
print(countrys)
print(numOfStudentsInClass)
print(gamma)
print(delta)
print(gamma)
print(omega)
print(alpha)

# tuples
# unchangeble
# ordered
# duplicates are ok
names = ("Tawanda", "Tatenda", "Angeline", "Stella", "Tafadzwa")
fruits = ("apple", "cherry", "watemelon", "peach", "guava")
grades = (10, 20, 59, 40, 36, 22)
countrys = ("Alabasta", "Dressrossa", "Elbaf", "Skypia")
numOfStudentsInClass = (39, 40, 30, 49,29)
beta = ("apple", "cherry", "watemelon", 39, 40, 30, "Alabasta", "Dressrossa", "Elbaf",)
delta = ("whatsapp", "instagram" , 500 , True, 0.003)
omega = ("superman", "batman", "wonderwoman", "cyborg", "greenarroew", "flash")
gamma = (True, "aquaman", "goku" )
alpha = (0.00, 300, 400, 1.22)

print(grades)
print(names)
print(fruits)
print(countrys)
print(numOfStudentsInClass)
print(gamma)
print(delta)
print(gamma)
print(omega)
print(alpha)

# #dictionaries
person = {"name": "Alice", "age": 25, "city": "New York"}
print(person["name"])  

students = {
    "John": {"math": 85, "science": 90},
    "Jane": {"math": 78, "science": 95}
}
print(students["Jane"]["science"]) 

grades = {"Alice": [85, 90, 88], "Bob": [78, 81, 85]}
print(grades["Alice"])  

person = {"name": "Bob", "age": 30}
person["job"] = "Engineer"
print(person)  

person = {"name": "Alice", "age": 25}
person["age"] = 26
print(person)  

car = {"brand": "Toyota", "model": "Corolla", "year": 2020}
del car["model"]
print(car)  

data = {"apple": 3, "banana": 5}
if "apple" in data:
    print("Apple is present")  

person = {"name": "Alice", "age": 25, "city": "New York"}
for key, value in person.items():
    print(key, ":", value)

a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}
a.update(b)
print(a)  

numbers = {x: x**2 for x in range(5)}
print(numbers)  


# if statements/ conditional statements/#inputs
age = 50
if age == 50:
    print(age)
else:
    print("err")

passcode = input("enter passcode: ")
if passcode == "1738":
 print("correct")
else:
 print("error")

weight = input ("step pn scale:")
if weight <= "50":
 print("unfit")
elif weight >= "300":
 print("over weight")
else:
 print("good")

day = input("Enter Day: ").lower()   
if day == "monday":
   print("wear uniform")
elif day == "tuesday":
   print("wear garments")
elif day == "wednesday":
   print("wear shorts")
elif day == "thursday":
   print("wear jeans")
elif day == "friday":
   print("wear t-shirt")
elif day == "saturday":
   print("wear hoodie")
elif day == "sunday":
   print("wear jacket")

days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
day = input("Enter Day: ").lower()  
if day in days:
   print(f"{day} is a valid day.")
else:
   print(f"{day} is not a valid day.")

username = "Tawanda"
password = 1234
age = 18
username = input("Enter username: ")
password = int(input("Enter password: "))
age = int(input("Enter age: "))        
if username == "Tawanda" and password == 1234 and age >= 20:
   print(f"Welcome {username}, you are {age} years old and your password is {password}.")
else:
   print("Access denied")

temparature = int(input("Enter the tempature: "))
sunny = input("Is it sunny? (yes/no): ").lower()
cold = input("Is it cold? (yes/no): ").lower()
temparature = 30
condition = (sunny == "yes" and temparature >= 30) or  (cold == "yes" and temparature < 20)
if sunny == "yes" and temparature >= 30:
   print(f"It's a sunny day, wear shorts.")
else:
   print(f"It's not cold day, wear long pants.") 

#operators
cats = 10
dogs = cats >= 6
catsAndDogs = dogs and cats < 15
print(catsAndDogs)
apples = 12
oranges = 8
peaches = apples and oranges >= 15
apples_oranges_peaches = apples and oranges and peaches < 20
print(apples_oranges_peaches)
isHuman = True
isAlien = False
result = isAlien or isHuman
print(result)
isWarm = False
isCold = True
result = isWarm or isCold
print(result)
isHuman = False
result = not isHuman
print(result)
speed = 12
isFast = speed >= 7
isAtheletic = True
result = isFast and (isAtheletic or speed < 10)
print(result)
price = 30
colour = "white"
isCorrctPrice = price == 30
isCorrctColour = colour == "white"
results = isCorrctPrice and isCorrctColour
print(results)

# loops
#for loop is used to iterate over a sequence (list, tuple, dictionary, set, string or range)
fruits = ["a","b","c","d","e"]
for fruit in fruits:
    print(fruit)

numbers = "123456789"
for num in numbers:
    print(num)

text = "Python"
for char in text:
    print(char)

grades = [10, 20, 59, 40, 36, 22]
for grade in grades:
    print(grade)

countrys = ["Alabasta", "Dressrossa", "Elbaf", "Skypia",]
for country in countrys:
    print(country)

omega = ("superman", "batman", "wonderwoman", "cyborg", "greenarroew", "flash")
for hero in omega:
    print(hero)

classs = (39, 40, 30, 49,29)
for x in classs:
    print(x)

omega = ("superman", "batman", "wonderwoman", "cyborg", "greenarroew", "flash")
for i in omega:
    print(i)

omega = {"superman", "batman", "wonderwoman", "cyborg", "greenarroew", "flash"}
for i in omega:
    print(i)

countrys = {"Alabasta", "Dressrossa", "Elbaf", "Skypia"}
for country in countrys:
    print(country)

# while loops
name = input("Enter your name: ")
while name == "":
    print("Error")
    name = input("Enter your name: ") 

i = 0
while i >  10:
    print(i)
    i += 1 
print("Done")

correct_number = 7
guess = int(input("Guess a number : "))
while guess != correct_number:
     print("Sorry thats not correct try again")
     guess = int(input("Guess a number : "))
print("You win")

correctNumber = 7
guess = int(input("Guess a number : "))
while True :
    if guess > correctNumber:
        print("You win")
        guess = int(input("Guess a number : "))
    elif guess < correctNumber:
        print("Too low")
        guess = int(input("Guess a number : "))
    else:
        print("Too high")
    guess = int(input("Guess a number : "))
print("You win")

carStarted = False
while True:
    command = input("Enter command (start/stop/quit/help): ").lower ()
    if command == "start":
        if carStarted == True:
            print("Car already started.")
        else:
            carStarted = True
            print("car started.")
    elif command == 'help':
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit
        """)
    elif command == "stop":
        if carStarted:
            carStarted = False
            print("car stopped.")
        else:
            print("car already stopped.")
    elif command == "quit":
        print("Exiting program.")
        break  # Exits the loop
    else:
        print("Invalid command. Use start, stop, or quit.")

carStarted = False
while True:
    command = input("Enter command (start/stop/quit): ")
    if command == "start":
        running = True
        print("Process started🤩.")
    elif command == "stop":
        running = False
        print("Process stopped✔.")
    elif command == "quit":
        print("Exiting program😢.")
        break
    elif command == 'help':
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit
        """)
    else:
        print("Invalid command.")

i = 10
while i <= 0:
    print(i)
    i -= 1 
print("Liftoff!")  

def greet():
    print("Hello!")
greet()  

def greet(name):
    print(f"Hello, {name}!")
greet("Alice")  

def square(num):
    return num * num
print(square(4))  

def greet(name="Guest"):
    print(f"Hello, {name}!")
greet()         
greet("Alice")  

def get_coordinates():
    return 10, 20
x, y = get_coordinates()
print(x, y) 

def add_numbers(*args):
    return sum(args)
print(add_numbers(1, 2, 3, 4)) 

def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
describe_person(name="Alice", age=25, job="Engineer")

square = lambda x: x * x
print(square(5)) 

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
print(factorial(5))  

def multiply_by_two(x):
    return x * 2
def apply_function(func, value):
    return func(value)
print(apply_function(multiply_by_two, 5))
