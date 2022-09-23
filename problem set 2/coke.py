def main():
    # promptingUser()
    claculateChange()

def promptUser():
    int_input = int(input('Enter Coin: '))
    return int_input

def verifyInput(int_userInput):
    # this function takes an integer and returns a boolean
    intList_ViableInputs = [25, 10, 5]
    if int_userInput in intList_ViableInputs:
        return True
    else:
        return False

# This function is a mess needs to be refactored
def claculateChange():
    totalPrice = 50
    remainingCoins = 50
    numberOfTries = 0
    while remainingCoins != 0:
        coinValue = promptUser()
        isViable = verifyInput(coinValue)
        if isViable:
            remainingCoins = remainingCoins - coinValue
            totalValueAccepted = totalPrice - remainingCoins
            print(f'Remaining Coins: {remainingCoins}')
        else:
            numberOfTries += 1
            print('Not Viable')

        if numberOfTries == 3:
            print(f'You Failed To Enter The Correct Value For {numberOfTries}')
            print(f'Here is Your ${totalValueAccepted}')
            break

if __name__ == "__main__":
    main()