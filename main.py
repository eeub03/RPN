from lib import RPN
import sys
if __name__ == "__main__":
    calculator = RPN()

    print(calculator.calculate(sys.argv[1]))