class Calculator:
    def _init_(self):
        self.num1 = int(input("Enter first number: "))
        self.num2 = int(input("Enter second number: "))
        self.choice = int(input("Enter choice\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n"))

    def calculate(self):
        if self.choice == 1:
            print("Addition =", self.num1 + self.num2)
        elif self.choice == 2:
            print("Subtraction =", self.num1 - self.num2)
        elif self.choice == 3:
            print("Multiplication =", self.num1 * self.num2)
        elif self.choice == 4:
            if self.num2 != 0:
                print("Division =", self.num1 / self.num2)
            else:
                print("Division by zero is not possible")
        else:
            print("Invalid Choice")

obj = Calculator()
obj.calculate()