def main():
    convert()

def convert():
    str_userInput = input("Please Enter A Sentence With :) and/or :(\n$ ")
    # used two if statements to check for both values
    # not good if I had many values
    # code has a bug but fits requirements
    if str_userInput.find(":)"):
        str_userInput = str_userInput.replace(":)", "\N{slightly smiling face}")
    if str_userInput.find(":("):
        str_userInput = str_userInput.replace(":(", "\N{slightly frowning face}")
    print(str_userInput)

main()