def main():
    didYouSayHello()

def didYouSayHello():
    str_userInput = input("Greeting: ").lower().lstrip()
    if str_userInput.startswith("hello"):
        print("$0")
    elif str_userInput.startswith("h"):
        print("$20")
    else:
        print("$100")
main()