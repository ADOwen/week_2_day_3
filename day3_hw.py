import module
# exercise 1 test

house_1 = module.square_feet(10, 10)

print(house_1)

circumference = module.get_circumference(2)

print(circumference)

module.is_finkle("Einhorn")

module.scouter(9001)


# exercise 2

# def shopping_cart():
#     cart = {}
#     while True:
#         question = input(
#             "Would you like to [S]how cart, [A]dd item [C]lear or [Q]uit? ")
#         if question.lower() == 's':
#             if cart:
#                 print(cart)
#             else:
#                 print('Your cart is empty')
#         if question.lower() == 'a':
#             item = input(
#                 "Please enter the item you would like to add to shopping cart: ")
#             quantity = input("How many would you like? ")
#             cart[item] = quantity
#         if question.lower() == 'c':
#             if cart:
#                 cart.clear()
#             else:
#                 print("Your cart is empty")
#         if question.lower() == 'q':
#             print("Here's your final order, thanks for shopping with us")
#             print('====================================================')
#             for item, quantity in cart.items():
#                 print(f"{quantity} {item.title()}")
#             break


# shopping_cart()
