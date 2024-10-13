import json
from user import UserManager
from product_inv import itemManager
from cart import Shopping_Cart
from admin import Admin
from data.initial_data import Inventory, users, active_sessions
from security_1 import Security
from api import The_Currency_Converter
from secure_api import run_secure_api
from insecure_api import run_insecure_api

# Main function to display all options on the command line
def main():
    security_1 = Security()
    users = {}
    user_manager = UserManager(users, security_1)
    user_manager.load_users()
    item_manager = itemManager(Inventory)
    admin = Admin(item_manager, user_manager)

    # API keys for currency converter
    api_key_secure = security_1.encrypt_data("a99d6ef2cc2590fc76ef15f8")  
    api_key_insecure = "a99d6ef2cc2590fc76ef15f8"  
    converter_secure = The_Currency_Converter(api_key_secure)
    converter_insecure = The_Currency_Converter(api_key_insecure)

    # Toggle for enabling or disabling security
    security_enabled = False  

    # Loop to display user options
    while True:
        print("Makeup LTD")
        print("1. Create Account")
        print("2. Login")
        print("3. Admin Login")
        print("4. Toggle Security Features")
        print("5. Run Secure/Insecure API")
        print("6. Exit")

        choice = input("Choose an option: ")

        # If statement to create username and password
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user_manager.create_user(username, password)

        # If statement to authenticate username and password
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = user_manager.authenticate(username, password)

            # If the user logs in successfully
            if user:
                print(f"Welcome, {user.username}!")
                cart = Shopping_Cart()

                while True:
                    print("\n1. Browse Products")
                    print("2. View Cart")
                    print("3. Checkout")
                    print("4. Convert Prices")
                    print("5. Logout")

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
                        currency_code = input("Enter the currency code (e.g., EUR, GBP, INR): ")
                        product_id = input("Enter product ID to convert price: ")

                        product_curr = item_manager.get_item(product_id)
                        if product_curr:
                            # Use secure or insecure converter based on security mode
                            converter = converter_secure if security_enabled else converter_insecure
                            converted_price = converter.convert_price(product_curr['price'], currency_code)

                            if converted_price:
                                print(f"The price in {currency_code} is {converted_price}")
                            else:
                                print("Could not convert the price.")
                        else:
                            print("Product not found.")

                    elif option == '5':
                        print("Logging out...")
                        break

            else:
                print("Invalid username or password.")

        # Admin login, checks admin credentials
        elif choice == '3':
            admin_username = input("Enter admin username: ")
            admin_password = input("Enter admin password: ")

            if admin_username == "admin" and admin_password == "admin123":
                print("Admin login successful.")
                admin.menu_admin()
            else:
                print("Invalid admin credentials.")

        # Toggle security features (only accessible by admins)
        elif choice == '4':
            admin_username = input("Admin username: ")
            admin_password = input("Admin password: ")

            if admin_username == "admin" and admin_password == "admin123":
                security_enabled = input("Enable security features? (yes/no): ").lower() == 'yes'
                security_1.toggle_security(security_enabled)
                print(f"Security features {'enabled' if security_enabled else 'disabled'}.")
            else:
                print("Only admins can toggle security features.")

        # Run secure or insecure API
        elif choice == '5':
            if security_enabled:
                admin_username = input("Admin username: ")
                admin_password = input("Admin password: ")

                if admin_username == "admin" and admin_password == "admin123":
                    print("Starting Secure API...")
                    run_secure_api()  
                else:
                    print("Only admin can run the secure API.")
            else:
                print("Starting Insecure API...")
                run_insecure_api()  

        elif choice == '6':
            break

if __name__ == "__main__":
    main()