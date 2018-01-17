def convert():
    cel = eval(input("What is the Celsius Temprature? "))
    fah = 9/5 * cel +32
    print("The Temperature is", fah, "degrees Fahrenheit.")

    # print warnings for extrem temps
    if fah > 90:
        print("It;s really hot there. Be carfu!")
    if fah < 30:
        print("Brrrr..It's freezing cold! Be sure to dress warm!")
convert()

