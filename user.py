import json
from security_1 import Security

class User:
    def __init__(self, username, password):
        # Initialise a new User with a username and password
        self.username = username
        self.password = password

class UserManager:
    def __init__(self, users, security):
        # Initialise UserManager with a dictionary of users and a security object
        self.users = users
        self.security = security

    def create_user(self, username, password):
        # Create a new user account with encrypted password
        if username in self.users:
            print("Username already exists!")
            return
        
        if not self.security.is_valid_password(password):
            print("Invalid password. It must meet the required criteria.")
            return

        # Encrypt the password before storing it
        encrypted_password = self.security.encrypt_password(password)
        
        
        print(f"Plaintext password: {password}")
        print(f"Hashed password: {encrypted_password}")

        self.users[username] = {
            "username": username,
            "password": encrypted_password
        }
        print("User account created successfully!")
        self.save_users()

    def authenticate(self, username, password):
        # Authenticate a user with the given username and encrypted password
        user = self.users.get(username)
        if user and self.security.decrypt_password(user['password']) == password:
            self.security.log_event(f"User {username} logged in successfully.")
            return User(username, password)
        self.security.log_event(f"Failed login attempt for {username}.")
        return None

    def delete_user(self, username):
        # Delete user account
        if username in self.users:
            del self.users[username]
            self.security.log_event(f"User {username} deleted.")
            print(f"User {username} deleted successfully.")
            self.save_users()
        else:
            print("User not found.")

    def update_user(self, username, new_password):
        # Update password for existing user
        if username in self.users:
            if not self.security.is_valid_password(new_password):
                print("Invalid password. It must meet the required criteria.")
                return

            # Encrypt the new password before updating
            encrypted_password = self.security.encrypt_password(new_password)

            print(f"Plaintext new password: {new_password}")
            print(f"Hashed new password: {encrypted_password}")

            self.users[username]['password'] = encrypted_password
            print("Password updated successfully!")
            self.save_users()
        else:
            print("User not found.")

    def generate_mfa_token(self, username):
        # Generate a random MFA token 
        mfa_token = "123456"  
        encrypted_mfa_token = self.security.encrypt_data(mfa_token)

        
        print(f"Plaintext MFA token: {mfa_token}")
        print(f"Hashed MFA token: {encrypted_mfa_token}")

        # Save the MFA token for the user
        self.users[username]['mfa_token'] = encrypted_mfa_token
        print(f"MFA token for {username} generated and hashed.")
        self.save_users()

    def save_users(self):
        # Save the users dictionary to a JSON file 
        with open('user.json', 'w') as f:
            json.dump(self.users, f, indent=4)
        
    def load_users(self):
        # Load the users from a JSON file into the users dictionary
        try:
            with open('user.json', 'r') as f:
                self.users = json.load(f)
                print("User data loaded from user.json.")
        except FileNotFoundError:
            print("user.json not found, starting with an empty user database.")