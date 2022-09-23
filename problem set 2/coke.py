def main():
    # promptingUser()
    claculateChange()

def promptUser():
    int_input = int(input('Insert Coin: '))
    return int_input

def verifyInput(int_userInput):
    # this function takes an integer and returns a boolean
    intList_ViableInputs = [25, 10, 5]
    if int_userInput in intList_ViableInputs:
        return True
    else:
        return False

def calculateAmountDue(amountDue, coinInserted):
    amountDue = amountDue - coinInserted
    return amountDue

def calculateInsertedTotal(insertedTotal, coinInserted):
    insertedTotal = insertedTotal + coinInserted
    return insertedTotal


# This function is a mess needs to be refactored
def claculateChange():
    insertedTotal = 0
    amountDue = 50
    numberOfTries = 0
    while amountDue != 0:
        coinInserted = promptUser()
        isViable = verifyInput(coinInserted)
        if isViable:
            amountDue = calculateAmountDue(amountDue, coinInserted)
            insertedTotal  = calculateInsertedTotal(insertedTotal, coinInserted)
            if insertedTotal > 50:
                changeOwed = amountDue * - 1
                print(f'Change Owed: {changeOwed}')
                # Ending Loop and returning Change
                break
            else:
                print(f'Amount Due: {amountDue}')
        else:
            numberOfTries += 1
            print('Not Viable')

        # Ending The Loop and Returning The Total Value Inserted To User
        if numberOfTries == 3:
            print(f'You Failed To Enter The Correct Value For {numberOfTries}')
            print(f'Here is Your ${insertedTotal}')
            break

if __name__ == "__main__":
    main()