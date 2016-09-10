def calculateWindchill(tempInCelsius, windForceBeaufort):
    return round(13 + 0.62 * tempInCelsius - 14 * windForceBeaufort**0.24
    + 0.47 * tempInCelsius * windForceBeaufort**0.24
    , 3)

def stringToTypeIfPossible(stringWithPossibleType):
    try:
        return int(stringWithPossibleType)
    except ValueError:
        return False

print("Welcome to the RealFeeling Temperature Calculator!")
print("Please type the temperature in Celsius: ")
while True:
    inputTemp = input("[-100 - 100]: ")
    fltInputTemp = stringToTypeIfPossible(inputTemp)
    if fltInputTemp is not False:
        break

print("Please type a number of windforce on the Scale of Beaufort: ")
while True:
    inputWindforce = input("[0 - 9]: ")
    fltWindforce = stringToTypeIfPossible(inputWindforce)
    if fltWindforce is not False:
        break

print("The RealFeeling Temperature is: ",
 calculateWindchill(fltInputTemp, fltWindforce),
 " degrees Celsius")
