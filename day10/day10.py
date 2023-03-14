# 1 Using function with return values

def format_name (f_name, l_name):
    return f"{f_name.title()} {l_name.title()}"

name = input ("name: ")
last_name = input ("Last name: ")

print (format_name(name, last_name))


# 2 Days in month

def is_leap(year):
    output = "yes"
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                 output = "yes"
            else:
                output = "no"
        else:
             output = "yes"
    else:
        output = "no"
    return output
    
year = int(input ("Please write the year: "))
leap = is_leap(year)
print (leap)
month = int(input("Insert the number of the month: "))


def days_in_month(leap, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    if leap == "yes":
        month_days[1] = 29
    return month_days[month-1]

days = days_in_month(leap, month)
print (days)


#  3 TEST!!! Calculator

def add (a,b):
    return a + b

def substrate (a,b):
    return a - b

def multiplicate (a,b):
    return a * b

def divide (a,b):
    return a / b

def calculator (a,b,operator):
    if operator == "+":
        return add (a,b)
    elif operator == "-":
        return substrate (a,b)
    elif operator == "*":
        return multiplicate(a,b)
    elif operator == "/":
        return divide (a,b)
    else:
        return "invalid"
    

more = "n" 

while not more == "end":

    if more == "n":   
        first_number = float (input ("What's the first number? "))
        operator = input ("+\n-\n*\n/\nPick an operator: ")
        second_number = float (input ("What's second number? "))

        result = calculator(first_number, second_number, operator)
        if result == "invalid":
            print ("You didn't input a valid operator.")
            more = "n"
        else:
            print (f"{first_number} {operator} {second_number} = {result}")
            more = input (f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, to finish type 'end': ")

    elif more == "y":
        print (f"The first number is {result}")
        operator = input ("+\n-\n*\n/\nPick an operator: ")
        second_number = float (input ("What's next number? "))
        result2 = result
        result = calculator(result, second_number, operator)

        if result == "invalid":
            print ("You didn't input a valid operator.")
            more = input (f"Type 'y' to continue calculating with {result2}, or type 'n' to start a new calculation, to finish type 'end': ")
            result = result2
        else:
            print (f"{result} {operator} {second_number} = {result}")
            more = input (f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, to finish type 'end': ")


print ("bye.")


# TEST TEACHER SOLUTION

from replit import clear
from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()