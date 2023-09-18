class Calculator:
    def __init__(self):
        self.number = int(input(' Please enter a number: '))

    def __add__(self, N):
        print(self.number + N.number)

    def __sub__(self, N):
        print(self.number - N.number)

    def __mul__(self, N):
        print(self.number * N.number)

    def __truediv__(self, N):
        print(self.number / N.number)

    def __pow__(self, N):
        print(self.number ** N.number)


n1 = Calculator()
print('+    -')
print('  ^  ')
print('*    /')
choice = input(' Choose one operator: ')
n2 = Calculator()
if choice == '+':
    n1 + n2
elif choice == '-':
    n1 - n2
elif choice == '*':
    n1 * n2
elif choice == '/':
    n1 / n2
elif choice == '^':
    n1 ** n2
else:
    print(' You entered invalid character.')