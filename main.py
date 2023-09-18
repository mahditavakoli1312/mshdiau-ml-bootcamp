def calculator():
    print("Welcome to the calculator!")
    print("Enter 'q' to quit.")

    while True:
        operation = input("please enter the operation (+, -, *, /)")
        if operation == 'q':
            print ( "GoodBye!" )
            break


            num1 = float(input("please enter the first number: "))
            num2 = float(input("please enter the second number: "))

            result = 0

            if operation == '+':
                result = num1 + num2
            elif operation == '-' :
                result = num1 - num2
            elif operation == '*' :
                result = num1 * num2
            elif operation == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("Error: division by zero!")
                    continue
                    print("result: ", result)
                    print("_____________________")
calculator()