# Functions assignment

# Area of a circle with input for radius

radius = float(input("Enter radius: \n"))
def areaOfCircleFunction(radius):
    area = 3.14159 * (radius ** 2)
    formatted = f"{area:.2f}"
    return formatted
print(areaOfCircleFunction(radius))

# Sales tax with input for item price

itemPrice = float(input("Enter item price: \n"))
tax = float(input("Enter tax: \n"))
def priceWithTax(itemPrice, tax):
    totalPrice = itemPrice + itemPrice * tax
    return totalPrice
print(priceWithTax(itemPrice, tax))

# Temperature from Fahrenheit to Celsius

fahrenheit = float(input("Enter Fahrenheit: \n"))
def tempConversionFhToCs(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius
print(tempConversionFhToCs(fahrenheit))

