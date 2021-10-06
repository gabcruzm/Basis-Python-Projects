def converter(currencies, dollar_value):
    pesos = float(input("How many " + currencies + " do you have?: "))
    dollars = round((pesos / dollar_value), 2)
    dollars = str(dollars)
    print("You have $" + dollars + " dollars")


menu = """
Welcome to the best currency converter !!!! 😜💵 

1. Colombian pesos COP
2. Argentine pesos ARS
3. Mexican pesos MXN

Choose an option: """

option = int(input(menu))

if option == 1:
    converter("Colombian pesos", 3875)
elif option == 2:
    converter("Argentine pesos", 65)
elif option == 3:
    converter("Mexican pesos", 24)
else:
    print("Please enter a valid option")



