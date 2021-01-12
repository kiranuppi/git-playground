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


with open("another_file", 'r') as f:
    lines = f.readlines()
    for x in range(0, len(lines)):
        print('Current Line:'+str(lines[x]))
        original_line = lines[x]
        new_line = original_line
        condition = False
        while condition is True:
            words = new_line.split()
            if words[1] == 'calc':
                output = calculate(words[3], words[2], words[4])
                new_line = lines[int(words[output]) - 1]
            else:
                new_line = lines[int(words[1])]
                if original_line == new_line:
                    condition = True
        print('Statement is :' + str(new_line))
        print('Line number :' + str(x))
