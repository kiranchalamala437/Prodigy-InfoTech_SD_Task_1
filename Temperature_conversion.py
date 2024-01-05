def main():
    temperature = float(input("Enter the value : "))

    originalUnit = input("Enter the measurement units (Celsius, Fahrenheit, Kelvin): ").lower()

    if originalUnit == "celsius":
        displayConvertedTemperatures1(temperature,originalUnit)

    elif originalUnit == "Fahrenheit":
        displayConvertedTemperatures2(temperature,originalUnit)

    else:
        displayConvertedTemperatures3(temperature,originalUnit)



def displayConvertedTemperatures1(temp, unit):
    convertedValue1 =  (temp* 9 / 5) + 32
    convertedValue2 = temp + 273.15
    print(str(temp) + " " + unit + " is equivalent to:")
    print(str(convertedValue1) + " Fahrenheit")
    print(str(convertedValue2) + " Kelvin")

def displayConvertedTemperatures2(temp, unit):
    convertedValue1 =  (temp - 32) * 5 / 9
    convertedValue2 = (temp - 32) * 5 / 9 + 273.15
    print(str(temp) + " " + unit + " is equivalent to:")
    print(str(convertedValue1) + " Celsius")
    print(str(convertedValue2) + " Kelvin")

def displayConvertedTemperatures3(temp, unit):
    convertedValue1 =  temp - 273.15
    convertedValue2 = (temp - 273.15) * 9 / 5 + 32
    print(str(temp) + " " + unit + " is equivalent to:")
    print(str(convertedValue1) + " Celsius")
    print(str(convertedValue2) + " Fahrenheit")

main()