def calculator():
    print("Simple Calculator Program")
    print("Follow the prompt to perform a simple math.")
    
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
   
    print("Choose an operation between +, -, * and /")
    operation = input("Enter the operation: ").strip()
  
    if operation == "+":
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}.")
    elif operation == "-":
        result = num1 - num2
        print(f"The result of {num1} - {num2} is {result}.")
    elif operation == "*":
        result = num1 * num2
        print(f"The result of {num1} * {num2} is {result}.")
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is {result}.")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Error: Invalid operation entered. Please use +, -, *, or /.")
        

calculator()
