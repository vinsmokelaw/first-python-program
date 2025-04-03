# making a simple calculator

def calculator():
    print("Omega calculator")
    print("USE: +, -, *, /  ")

forever = True

while forever:
    number1 = float(input("Enter number: "))
    operator = input("+, -, *, / ")
    number2 = float(input("Enter number: "))

    if operator == "+":
        print(number1 + number2)
    elif operator == "-":
        print(number1 - number2)
    elif operator == "*":
        print(number1 * number2)
    elif operator == "/":
        print(number1 / number2)
    else:
        print("wrong_operator use '+', '-', '*', '/',")



          