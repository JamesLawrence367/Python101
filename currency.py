# Shorter Version (No Error Handling)
from currency_converter import CurrencyConverter as c
changeFrom = input("Enter type of currency to convert from (GBP/USD/EUR):\n")
amount = float(input("Enter amount of money to convert:\n"))
changeTo = input("Enter type of currency to convert to (GBP/USD/EUR):\n")
print(c().convert(amount, changeFrom, changeTo))

# Longer Version (With Error Handling)
from currency_converter import CurrencyConverter as c
changeTo, changeFrom = "", ""
amount = False
while changeFrom not in ["GBP", "EUR", "USD",] or amount == False or changeTo not in ["GBP", "EUR", "USD",]:
    changeFrom = str(input("Enter the type of currency to convert from (GBP/EUR/USD): "))
    changeTo = str(input("Enter the type of currency to convert to (GBP/EUR/USD): "))
    try:
        amount = float(input("Enter the amount to convert: "))
    except:
        amount = False
print("The amount in", changeTo, "is", round(c().convert(amount, changeFrom, changeTo), 2))