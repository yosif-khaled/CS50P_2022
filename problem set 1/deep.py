def main():
    str_userInput = input(" Enter 42 for Yes Other for No.. \n$ ")
    if isInputFortyTwo(str_userInput) is True:
        print("Yes")
    else:
        print("No")

def isInputFortyTwo(str_userInput):
    str_userInput = str_userInput.lower().replace(" ", "")
    print(str_userInput)
    viableInputs =  ["42", "fortytwo", "forty-two"]
    # isViable asks if is there any value in the userInput that matches a value in the viableInputs list
    isViable = any(value in str_userInput for value in viableInputs)
    return isViable

main()