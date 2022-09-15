def main():
    massEnergyEquivalence()

def massEnergyEquivalence():
    str_userInput = input("Enter The Mass: ")
    int_userInput = int(str_userInput)
    const_int_lightSpeed =  300000000 # 299792458
    energy = (const_int_lightSpeed ** 2) * int_userInput
    print(energy)

main()