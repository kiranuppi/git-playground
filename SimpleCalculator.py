num1 = input("First Number:\n")
operator = input("Input operator (+, -, *, /, mod):\n")
num2 = input("Second Number:\n")


def calculate(num1, operator, num2):
    number1 = int(num1)
    number2 = int(num2)
    if operator == "+":
        return number1 + number2

    elif operator == "-":
        return number1 - number2
    elif operator == "*" or operator == "x" or operator == "X":
        return number1 * number2
    elif operator == "/":
        return number1 / number2
    elif operator == "mod":
        return number1 % number2
    else:
        return False


output = calculate(num1, operator, num2)
if not output:
    print('Can not perform the operation based on your input!!')
else:
    print("The calculated answer: " + str(output))