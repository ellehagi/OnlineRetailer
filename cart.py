class Shopping_Cart:
    # This method creates a new Shopping_Cart function.
    def __init__(self):
        # this list holds all of the shopping products
        self.prods = []

    def add_item(self, item_id, item_manager):
        # this variable gets all of the item details using item_manager's get_item method.
        product = item_manager.get_item(item_id)
        # if statement to check if the item is there
        if product:
            self.prods.append(product)
            print(f"Added {product['name']} to cart.")
        else:
            print("Could not add product to cart.")
    # method to see what items are in the cart
    def view_cart(self):
        print("Your Shopping Cart:")
        # loop over each item in the list to show details
        for prod in self.prods:
            print(f"Product ID: {prod['id']}, Name: {prod['name']}, Price: {prod['price']}")
    # method to checkout and calculate the total amount
    def checkout(self):
        total = sum(prod['price'] for prod in self.prods)
        print(f"Total amount: ${total:.2f}")
        # clear the shopping cart
        self.prods.clear()
        print("Checked out successfully.")