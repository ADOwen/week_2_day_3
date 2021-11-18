import module
# exercise 1 test

house_1 = module.square_feet(10, 10)

print(house_1)

circumference = module.get_circumference(2)

print(circumference)

module.is_finkle("Einhorn")

module.scouter(9001)


# exercise 2

def shopping_cart():
    cart = {}
    while True:
        question = input(
            "\nWould you like to [S]how cart, [A]dd item [C]lear or [Q]uit? ")
        if question.lower() == 's':
            if cart:
                for item, quantity in cart.items():
                    print(f"\n{quantity} : {item.title()}")
            else:
                print('\nYour cart is empty')
        if question.lower() == 'a':
            item = input(
                "\nPlease enter the item you would like to add to shopping cart: ")
            quantity = input("\nHow many would you like? ")
            cart[item] = quantity
        if question.lower() == 'c':
            if cart:
                cart.clear()
                print("\nYour cart has been cleared")
            else:
                print("\nYour cart is empty")
        if question.lower() == 'q':
            if cart:
                print("\nHere's your final order, thanks for shopping with us")
                print('====================================================')
                for item, quantity in cart.items():
                    print(f"\n{quantity} : {item.title()}")
                break
            else:
                print("\nSorry you couldn't find anything, have a great day!")
                break


shopping_cart()
