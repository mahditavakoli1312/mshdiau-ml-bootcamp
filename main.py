def cal(value1,operand,value2):
    if(operand == '+'):
        return value1 + value2
    elif(operand == '-'):
        return value1 - value2
    elif (operand == '*'):
        return value1 * value2
    elif (operand == '/'):
        return value1 / value2

val1,op,val2 = input("Enter value1,operand and valu2:")
val1 = int(val1)
val2 = int(val2)
print(cal(val1,op,val2))