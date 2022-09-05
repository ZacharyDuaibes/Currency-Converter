import math
# Taking input from user to define variables
startCurrency = str(input("Enter the starting currency (CAD, USD, EURO): ")).upper()
convertCurrency = str(input("Enter the currency to convert to (CAD, USD, EURO): ")).upper()
amountConversion = float(input("Enter the amount of " + startCurrency + " to convert to " + convertCurrency + ": "))
print()
# If starting currency is "CAD", then it will run each line of code until the users desired currency to covert to is met 
if startCurrency == "CAD":
    if convertCurrency == "USD":
        total = amountConversion * 0.78
        print("%.2f" % amountConversion, startCurrency, "= %.2f" % total, convertCurrency)
    elif convertCurrency == "CAD":
        print("%.2f" % amountConversion, startCurrency, "= %.2f" % amountConversion, convertCurrency)
    else:
        total = amountConversion * 0.70
        print("%.2f" % amountConversion, startCurrency, "= %.2f" % total, convertCurrency)
# If starting currency is "USD", then it will run each line of code until the users desired currency to covert to is met 
if startCurrency == "USD":
    if convertCurrency == "CAD":
        total = amountConversion / 0.78
        print("%.2f" % amountConversion, startCurrency, "= %.2f" % total, convertCurrency)
    elif convertCurrency == "USD":
        print("%.2f" % amountConversion, startCurrency, "= %.2f" % amountConversion, convertCurrency)
    else:
        total = (amountConversion / 0.78) * 0.70
        print("%.2f" % amountConversion, startCurrency, "= %.2f" % total, convertCurrency)
# If starting currency is "EURO", then it will run each line of code until the users desired currency to covert to is met 
if startCurrency == "EURO":
    if convertCurrency == "CAD":
        total = amountConversion / 0.70
        print("%.2f" % amountConversion, startCurrency, "= %.2f" % total, convertCurrency)
    elif convertCurrency == "EURO":
        print("%.2f" % amountConversion, startCurrency, "= %.2f" % amountConversion, convertCurrency)
    else:
        total = amountConversion / 0.70 * 0.78
        print("%.2f" % amountConversion, startCurrency, "= %.2f" % total, convertCurrency)

