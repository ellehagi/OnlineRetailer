class Admin:
    # Initialize Admin with item_manager and user_manager instances.
    def __init__(self, item_manager, user_manager):
        self.item_manager = item_manager
        self.user_manager = user_manager

#Main function that serves to display all of the items on command line
    def menu_admin(self):
        #loop thats diplays user options
        while True:
            print("\nAdmin Menu:")
            print("1. Add Product")
            print("2. Update Product")
            print("3. Delete Product")
            print("4. Create User")
            print("5. Delete User")
            print("6. Exit Admin Menu")

            choice = input("Choose an option: ")
            # Get product details and add to the item manager.
            if choice == '1':
                name_1 = input("Enter product name: ")
                price_1 = float(input("Enter product price: "))
                self.item_manager.add_item(name_1, price_1)

             # Get product id and new details for updating.
            elif choice == '2':
                item_id = input("Enter product ID to update: ")
                name_1 = input("Enter new product name (leave blank to keep current): ")
                price_1 = input("Enter new product price (leave blank to keep current): ")
                price_1 = float(price_1) if price_1 else None
                self.item_manager.update_item(item_id, name_1 if name_1 else None, price_1)
             # Get product id and delete the product.
            elif choice == '3':
                item_id = input("Enter product ID to delete: ")
                self.item_manager.delete_item(item_id)
            # Get user details to create a new user.
            elif choice == '4':
                username = input("Enter username for new user: ")
                password = input("Enter password for new user: ")
                self.user_manager.create_user(username, password)
            # Get username and delete the user.
            elif choice == '5':
                username = input("Enter username to delete: ")
                self.user_manager.delete_user(username)

            elif choice == '6':
                break