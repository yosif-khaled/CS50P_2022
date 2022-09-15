# Constants
int_LIGHT_SPEED =  300000000 # 299792458

def main():
    energyEquivalentToMass()

def energyEquivalentToMass():
    str_userInput = input("Enter The Mass: ")
    int_userInput = int(str_userInput)
    energy = (int_LIGHT_SPEED ** 2) * int_userInput
    print(energy)

main()