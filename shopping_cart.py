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
