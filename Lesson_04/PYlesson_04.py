item1 = input("Please enter item 1: ")
Price1 = float(input("Please enter the price: "))

item2 = input("Please enter item 2: ")
Price2 = float(input("Please enter the price: "))

item3 = input("please enter item 3: ")
Price3 = float(input("Please enter the price: "))

Total = ("Total:")

Subtotal = ("Subtotal:")

Sub = (Price1 + Price2 + Price3)

Tax = ("Tax:")

Taxes = (Sub * 0.07)

print("<" * 15, "Recipt", ">" * 15)
print("\n")

def printLine(left, right): #Prints each individual line in the recipt
    print("* {:<15}.....{:>15.2f} *".format(left, right))
                                    

printLine(item1, Price1)
printLine(item2, Price2)
printLine(item3, Price3)
print("\n")
printLine(Subtotal, Sub)
printLine(Tax, Taxes)
printLine(Total, Sub + Taxes)

print("-" * 38)
print("* Thank you for your support *")

















