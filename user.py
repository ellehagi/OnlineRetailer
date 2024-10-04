from security_1 import Security

class User:
    def __init__(self, username, password):
         # Initialize a new User with a username and password
        self.username = username
        self.password = password

class UserManager:
    def __init__(self, users, security):
        # Initialize UserManager with a dictionary of users and a security object
        self.users = users
        self.security = security

    def create_user(self, username, password):
         # Create a new user account
        if username in self.users:
            print("Username already exists!")
            return
        
        if not self.security.is_valid_password(password):
            return
        # Encrypt the passwords before storing it
        encrypted_password = self.security.encrypt_password(password)
        self.users[username] = User(username, encrypted_password).__dict__
        print("User account created successfully!")

    def authenticate(self, username, password):
        # Authenticate a user with the given username and password
        user = self.users.get(username)
        if user and self.security.decrypt_password(user['password']) == password:
            self.security.log_event(f"User {username} logged in successfully.")
            return User(username, password)
        self.security.log_event(f"Failed login attempt for {username}.")
        return None

    def delete_user(self, username):
        # delete user account
        if username in self.users:
            del self.users[username]
            self.security.log_event(f"User {username} deleted.")
            print(f"User {username} deleted successfully.")
        else:
            print("User not found.")

    def update_user(self, username, new_password):
        # update password for existing user
        if username in self.users:
            if not self.security.is_valid_password(new_password):
                return
            
            # Encrypt the new password before updating
            encrypted_password = self.security.encrypt_password(new_password)
            self.users[username]['password'] = encrypted_password
            print("Password updated successfully!")
        else:
            print("User not found.")