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
num1 = float(input("enter a number :"))
operator = input("select the operator (+, -, *, /):")
num2 = float(input("enter a number :")) 

result = calculate(num1,operator,num2)
print(f"{num1} {operator} {num2} = {result}")