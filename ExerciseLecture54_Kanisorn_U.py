def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "admin" and password == "1234":
        return True
    else:
        return False
def showMenu():
    print(15*"-" + "Menu" + 15*"-")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    print("Choose 1 or 2")
def menuSelect():
    userSelected = input(">>")
    if userSelected == "1":
        print("Vat Price = ", vatCalculate(int(input("Price : "))), "Baht")
    elif userSelected == "2":
        print("Total Price = ", priceCalculate(), "Baht")
    return
def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result
def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculate(price1 + price2)

if login() == True:
    showMenu()
    menuSelect()
else:
    print("Try again !!")