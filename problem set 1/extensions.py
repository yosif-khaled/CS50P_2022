### WARNING ###
# the application assumes that the user input will be valid
# in this formula :: file-name.extension // file.extension // file name.extension

def main():
    str_userInput = input("File Name: ")
    str_fileExtension = fileExtension(str_userInput)
    printFileType(str_fileExtension)

def fileExtension(str_userInput):
    str_userInput = str_userInput.lower().split(".")
    int_stringLength = len(str_userInput)
    str_ext = f"{str_userInput[int_stringLength - 1]}"
    return str_ext

def printFileType(str_ext):
    match str_ext:
        case "gif":
            print("image/gif")
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")

# main()

while True:
    main()