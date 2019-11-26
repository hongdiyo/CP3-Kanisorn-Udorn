userInput = int(input("Cost : "))
def vatCal(userInput):
    Total = userInput*7/100 + userInput
    return Total
print(vatCal(userInput))
