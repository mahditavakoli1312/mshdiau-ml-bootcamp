number_1 = int(input("Enter your the first number: "))
number_2 = int(input("Enter your the second number: "))
operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')
if operation == '+':
    output_number = number_1 + number_2
    print( "{} + {} = {}" .format(number_1, number_2, output_number))
elif operation == '-':
    output_number = number_1 - number_2
    print( "{} - {} = {}" .format(number_1, number_2, output_number))
elif operation == '*':
    output_number = number_1 * number_2
    print( "{} * {} = {}" .format(number_1, number_2, output_number))
elif operation == '/':
    output_number = number_1 / number_2
    print( "{} / {} = {}" .format(number_1, number_2, output_number))
else:
    print('You have not typed a valid operator, please run the program again!!!')