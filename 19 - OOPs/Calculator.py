# Problem 9: Create a Calculator class with add(), subtract(), multiply(), and divide() methods.
# Each method accepts two numbers and returns the result.
#
# Goal: Group related operations inside a class.

class Calculator:
    def __init__(self,number1, number2):
        self.number1 = number1
        self.number2 = number2

    def addition(self):
        return self.number1 + self.number2
    def subtraction(self):
        return self.number1 - self.number2
    def multiplication(self):
        return self.number1 * self.number2
    def division(self):
        return self.number1 / self.number2

q1 = Calculator(1,2)
sum = q1.addition()
multi = q1.multiplication()
div = q1.division()
sub = q1.subtraction()
print(sum,multi,div,sub,sep="\n")