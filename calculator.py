'''num1 = input("First Number:\n")
operator = input("Input operator (+, -, *, /):\n")
num2 = input("Second Number:\n")
'''


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
    else:
        return False


with open("inputFile.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        words = line.split()
        operator = words[1]
        num1 = words[2]
        num2 = words[3]
        calculate(num1, operator, num2)

        output = calculate(num1, operator, num2)
        if output == False:
            print('Can not perform the operation based on your input!!')
        else:
            print("The calculated answer: " + str(output))
