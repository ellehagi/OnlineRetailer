import json
from user import UserManager
from product_inv import itemManager
from cart import Shopping_Cart
from admin import Admin
from data.initial_data import Inventory, users, active_sessions
from security_1 import Security

#Main function that serves to display all of the items on command line
def main():
    security_1 = Security()  
    user_manager = UserManager(users, security_1)
    item_manager = itemManager(Inventory)
    admin = Admin(item_manager, user_manager)

#loop thats diplays user options
    while True:
        print("Makeup LTD")
        print("1. Create Account")
        print("2. Login")
        print("3. Admin Login")
        print("4. Toggle Security Features")
        print("5. Exit")

        choice = input("Choose an option: ")
      # if statement to create username and password
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user_manager.create_user(username, password)
      # if statement to authenticate username and password
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = user_manager.authenticate(username, password)
           # if statement for when the user logins
            if user:
                print(f"Welcome, {user.username}!")
                cart = Shopping_Cart()
                while True:
                    print("\n1. Browse Products")
                    print("2. View Cart")
                    print("3. Checkout")
                    print("4. Logout")
                    option = input("Choose an option: ")

                    if option == '1':
                        item_manager.display_items()
                        product_choice = input("Enter product ID to add to cart or '0' to go back: ")
                        if product_choice != '0':
                            cart.add_item(product_choice, item_manager)

                    elif option == '2':
                        cart.view_cart()

                    elif option == '3':
                        cart.checkout()

                    elif option == '4':
                        print("Logging out...")
                        break

            else:
                print("Invalid username or password.")
  # if statement for admin, it checks to see if the admin has the right credentials
        elif choice == '3':
            admin_username = input("Enter admin username: ")
            admin_password = input("Enter admin password: ")
            if admin_username == "admin" and admin_password == "admin123":
                print("Admin login successful.")
                admin.menu_admin()
            else:
                print("Invalid admin credentials.")
       # this if statement enables sercurity features 
        elif choice == '4':
            security_enabled = input("Enable security features? (yes/no): ").lower() == 'yes'
            security_1.toggle_security(security_enabled)

        elif choice == '5':
            break

if __name__ == "__main__":
    main()