print("Answer the following information about the book you are selling: ")
name = input("Name of the Book: ")
id = int(input("Book ID: "))
price = float(input("Price: "))
free_shipping = (input("The delivery is free? (Yes/No): "))
free_shipping = free_shipping.capitalize()
free_shipping = free_shipping.strip()

# if free_shipping == "Yes":
#     free_shipping = True
# elif free_shipping == "No":
#     free_shipping = False
# else:
#     print("Incorrect value, Please write Yes or No")

print(f"""
    Name: {name} 
    Id: {id}
    Price: {price}
    Free Shipping: {free_shipping}
""")
