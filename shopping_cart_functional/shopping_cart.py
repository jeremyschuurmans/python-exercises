cart_items = []
cart_prices = []

# Tracking total prices so we can display price and quantity
# The price displayed should be the individual price
# but when the cart is totalled, the total should reflect multiple
# quantities if there are any.
total_prices = []
cart_quantities = []

menu = """
Please select one of the following:
1. Add item(s)
2. View cart
3. Remove item
4. Compute total
5. Quit
"""

user_selection = ""

def display_cart(cart_items, cart_prices, cart_quantities):
    # Headers for cart display formatted left, middle, and right
    print(f"{'Selection':<10}{'Item':^20}{'Price':>10}{'Quantity':>20}")
    for i in range(len(cart_items)):
        item = cart_items[i]
        price = f"${cart_prices[i]:.2f}"
        quantity = cart_quantities[i]

        # Cart contents formatted to align with headers
        print(f"{i+1:<10}{item:^20}{price:>10}{quantity:>20}")

def cart(user_selection):
    while user_selection != "5":
        print(menu)

        user_selection = input("Please enter an action: ")

        if user_selection == "1":
            item = input("What item would you like to add? ")
            price = total_price = float(input(f"What is the price of {item}? $"))
            quantity = int(input(f"How many would you like to add? "))

            # Adjusting the price for multiples of the same item
            if quantity > 1:
                total_price = total_price * quantity

            cart_items.append(item)
            cart_prices.append(price)
            total_prices.append(total_price)
            cart_quantities.append(quantity)

            print(f"{item} has been added to your cart.")

        elif user_selection == "2":
            if len(cart_items) > 0:
                print("The contents of your shopping cart are:")

                display_cart(cart_items, cart_prices, cart_quantities)
            # If there are no items in the cart, we want to inform the user rather than print empty contents
            else:
                print("Your cart is currently empty.")

        elif user_selection == "3":
            if len(cart_items) != 0:
                if len(cart_items) > 1:
                    display_cart(cart_items)

                    index_to_remove = int(input(f"Which item would you like to remove? Please enter 1-{len(cart_items)}: ")) - 1
                    item_to_remove = cart_items[index_to_remove]

                    cart_items.pop(index_to_remove)
                    cart_prices.pop(index_to_remove)
                    total_prices.pop(index_to_remove)
                    cart_quantities.pop(index_to_remove)
                else:
                    item_to_remove = cart_items[0]

                    cart_items.pop()
                    cart_prices.pop()
                    total_prices.pop()
                    cart_quantities.pop()

                print(f"{item_to_remove} has been removed from your cart.")
            else:
                print("Your cart is currently empty.")

        elif user_selection == "4":
            total = sum(total_prices)

            print(f"The total price of the items in your cart is: ${total:.2f}")

    print("Thank you. Goodbye!")

cart(user_selection)
