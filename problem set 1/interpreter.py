def main():
    str_userInput = input("Expression: ")
    mathInterpreter(str_userInput)

def mathInterpreter(str_userInput):
    ## this function assumes that the user input will be
     # formated as follows :: x y z, separated by a single
     # space character where x, z are numbers
     # y is the operator + or - or * or /
    input_list = str_userInput.lstrip().split(" ")
    # add an if statement to catch invalid input
    if len(input_list) <= 2:
        print("The Input is Invalid")
    else:
        float_first = float(input_list[0])
        str_operator = input_list[1]
        float_second = float(input_list[2])
        operatorAssignment(float_first, str_operator, float_second)

def operatorAssignment(float_first, arithmaticOperator, float_second):
    match arithmaticOperator:
        case "+":
            ouput = round((float_first + float_second), 1)
            print(ouput)
        case "-":
            output = round((float_first - float_second), 1)
            print(output)
        case "*":
            output = round((float_first * float_second), 1)
            print(output)
        case "/":
            output = round((float_first / float_second), 1)
            print(output)
        case _:
            print("Input is not valid")

main()