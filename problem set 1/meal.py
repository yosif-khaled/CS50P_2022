def main():
    str_userInput = input("What time is it? ")
    mealTime(convert(str_userInput))

def isItPM(time):
    time_list = time.lower().split(" ")
    addTwelve = False
    if time_list[-1] == "p.m.":
        addTwelve = True
    else:
        addTwelve = False
    return addTwelve

def convert(time):
    # I don't think it is necessary to convert minutes
    # only did it to fit problem set requirements
    time_list = time.replace(" ", ":").split(":")
    if isItPM(time):
        int_hours = int(time_list[0]) + 12
    else:
        int_hours = int(time_list[0])

    float_minutes = int(time_list[1]) / 60
    convertedTime = int_hours + float_minutes
    return convertedTime

def mealTime(time):
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")
    else:
        print("No meals in that time")
    

if __name__ == "__main__":
    main()

# breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00.