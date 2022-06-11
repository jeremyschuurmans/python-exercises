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

def display_cart(cart_items):
    # Headers for cart display formatted left, middle, and right
    print(f"{'Selection':<10}{'Item':^20}{'Price':>10}{'Quantity':>20}")
    for i in range(len(cart_items)):
        item = cart_items[i]
        price = f"${cart_prices[i]:.2f}"
        quantity = cart_quantities[i]

        # Cart contents formatted to align with headers
        print(f"{i+1:<10}{item:^20}{price:>10}{quantity:>20}")
