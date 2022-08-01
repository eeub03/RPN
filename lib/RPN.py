import operator
from collections import deque
import sys
class RPN:
    def __init__(self):
        self.operators = {"+": operator.iadd, "-" : operator.isub, "*": operator.imul, "/": operator.ifloordiv,
                          "%": operator.imod}

    def calculate(self, cli):
        """Function that performs RPN on a command line input"""
        stack = deque()
        # Loop over each argument in the CLI.
        # An input of "6 4 \" would loop 3 times with 6, 4 and \ being "value".
        for value in cli.split(" "):
            try:
                if value in self.operators:
                    # When value is one of the operators, perform that operation on the top two values in the stack.
                    x,y = stack.pop(), stack.pop()
                    answer = self.operators[value](y,x)
                else:
                    answer = int(value)
                stack.append(answer)
            except ValueError:
                raise ValueError("Input must be a whole number")
            except ZeroDivisionError:
                raise ZeroDivisionError("Cannot divide values by zero")
        return stack.pop()


if __name__ == "__main__":
    calculator = RPN()

    print(calculator.calculate(sys.argv[1]))