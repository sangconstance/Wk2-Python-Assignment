def user_input():
    #Get user to enter some values
    num1= int(input("Enter your first value: "))
    num2= int(input("Enter your second value: "))
    operation =input("Enter an operation(+,-,*):")

    #Perform the cosen operation
    if  operation == '+' :
        result = num1 +num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '-' :
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '/':
          if num2 != 0:
              result = num1 / num2
              print(f"{num1} / {num2} = {result}")
          else:
              print("Error: Divison by zero is not alowed.")
    else :
        print("Invalid operation. Please use +, -, *, or /.")
user_input()

      
      


        