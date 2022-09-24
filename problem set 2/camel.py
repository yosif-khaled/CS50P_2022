def main():
    convertToSnake()

# I need to find a way to check the first character before


def convertToSnake():
    str_userInput = input("Camel Case: ")
    print("snake_case: ", end=" ")
    for c in str_userInput:
        if c.isupper():
            c = c.lower()
            print(f"_{c}", end="")
        else:
            print(c, end="")
    print("\n")


# main()
while True:
    main()
