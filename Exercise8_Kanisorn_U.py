username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Welcome to iSHOP")
    print("-------------------------------------")
    print("1) Banana               1         $")
    print("2) Apple                1.25      $")
    print("3) Orange               1.28      $")
    print("-------------------------------------")
    print("Price including vat\n")

    goods  = float(input("Select: "))
    number = float(input("Quantity ?: "))

    if   goods == 1:
         price = 1
         print("\nTotal($): ", price * number)
         print("\n------------You’re Welcome-----------")
    elif goods == 2:
         price = 1.25
         print("Total($): ", price * number)
         print("\n------------You’re Welcome-----------")
    elif goods == 3:
         price = 1.28
         print("Total($): ", price * number)
         print("\n------------You’re Welcome-----------")

