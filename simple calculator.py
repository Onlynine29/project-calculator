# Simple Python Calculator
# Author: Varun Goud
# Description: Performs basic arithmetic (+, -, *, /) between two numbers

# Define the main calculation logic
def calculate(num1,operator,num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0 :
          return "cannot divide by zero"
        return num1 / num2
    else:
        return "invalid operator"
# Take inputs from the user
num1 = float(input("enter a number :"))
operator = input("select the operator (+, -, *, /):")
num2 = float(input("enter a number :")) 

# Perform the calculation
result = calculate(num1,operator,num2)
# Display the result
print(f"{num1} {operator} {num2} = {result}")
