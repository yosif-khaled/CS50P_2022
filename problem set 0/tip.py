### WARNING ###
# THIS CODE WAS WRITTEN ASSUMING THE USER WILL INPUT VALUES IN EXPECTED FORMATS

def main():
    float_dollars = dollars_to_float(input("How much was the meal? "))
    # print(type(float_dollars))
    float_percent = percent_to_float(input("What percentage would you like to tip? "))
    # print(type(float_percent))
    tip = float_dollars * float_percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(str_dollars):
    str_dollars = str_dollars.replace("$", "")
    return float(str_dollars)


def percent_to_float(str_percent):
    str_percent = str_percent.replace("%", "")
    return float(str_percent)/100

main()