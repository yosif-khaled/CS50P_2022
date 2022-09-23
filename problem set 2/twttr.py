def main():
    userInput: str = input('Input: ')
    output: str = removeVowels(userInput)
    print(f'Output: {output}')

def removeVowels(input: str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for v in input:
        if v in vowels:
            input = input.replace(f'{v}', '')
        else:
            continue
    return input

if __name__ == "__main__":
    main()