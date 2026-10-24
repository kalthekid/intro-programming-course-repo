#Taco palace menu ordering program

print("Welcome to Taco Palace, please view the menu below and enter the number that represents your selection.")

menuList = ["1. Taco", "2. Enchiladas", "3. Chips", "4. Churros", "5. Quit"]
priceList = [float(2.95), float(7.95), float(1.95), float(5.95)]
customerOrder = []
totalPrice = 0
def menu():
    return menuList

print(menu())

customerChoice = int(input("Enter your choice: "))

while(customerChoice != 5):
    if  customerChoice == 1:
        print("You have selected Taco")
        print(priceList[0])
        totalPrice = totalPrice + priceList[0]
        customerOrder.append("Taco")
    elif customerChoice == 2:
        print("You have selected Enchiladas")
        print(priceList[1])
        totalPrice = totalPrice + priceList[1]
        customerOrder.append("Enchiladas")
    elif customerChoice == 3:
        print("You have selected Chips")
        print(priceList[2])
        totalPrice = totalPrice + priceList[2]
        customerOrder.append("Chips")
    elif customerChoice == 4:
        print("You have selected Churros")
        print(priceList[3])
        totalPrice = totalPrice + priceList[3]
        customerOrder.append("Churros")
    else:
        print("Invalid Choice")
    print(menu())
    customerChoice = int(input("Enter your choice: "))

print("Thank you for ordering," + str(customerOrder))
print("$", totalPrice, sep="")