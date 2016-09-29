'''
    Notes:
    Could probably clean up this code some more by changing up
    the functions sumOfOddPositionsRightToLeft and luhnStepTwoAndThree.
    The loops used inside these functions are pretty much identical.
    Only the code inside of them differs slightly. I am not willing to spend
    the time on this right now though..

    - xoxo, Peter

'''

CARD_MAX_NUMBERS = 19

def getUserCardNumber() :
    userInput = input("Card Number: ")
    lenUserInput = len(userInput)
    if lenUserInput > CARD_MAX_NUMBERS:
        print("The cardnumber you entered contained more than the maximum amount"\
            "of characters.\nEntered:", lenUserInput,
            ", Maximum:", CARD_MAX_NUMBERS)
        return getUserCardNumber() # request the card number again

    try:
        return int(userInput) # return the userInput card number in integer form
    except ValueError:
        print("The cardnumber you entered contained invalid characters.\n"\
            "Please ensure to only enter numbers.")
        return getUserCardNumber() # request the card number again

def sumOfOddPositionsRightToLeft(strInput):
    total = 0
    for x in range(1, len(strInput)+1): # 1 to 4, because we count right to left
        if x % 2 == 0: # skip even numbers
            continue
        total += int(strInput[-x])
    return total

def luhnStepTwoAndThree(strInput): # meh :\ function name
    sum = 0
    for x in range(1, len(strInput)+1):
        if x % 2 != 0: # skip odd numbers
            continue
        doubledNumber = (int(strInput[-x]) * 2)
        if doubledNumber >= 10:
            doubledNumber = ( int(str(doubledNumber)[0]) \
                + int(str(doubledNumber)[1]) )
        sum += doubledNumber
    return sum

print("Credit card number checker program.")
cardNumber = str(getUserCardNumber())

luhnStepOne = sumOfOddPositionsRightToLeft(cardNumber)
luhnStepTwoAndThree = luhnStepTwoAndThree(cardNumber)
luhnStepFour = luhnStepOne + luhnStepTwoAndThree
if luhnStepFour % 10 == 0:
    print("This credit card number is valid according to the Luhn algorithm.")
else:
    print("This credit card number is not valid according to the Luhn algorithm")
