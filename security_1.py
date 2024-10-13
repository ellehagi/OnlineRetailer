import re
from cryptography.fernet import Fernet
import logging

# Set up logging to write logs to 'event_log.txt'
logging.basicConfig(filename='event_log.txt', level=logging.INFO)

class Security:
    def __init__(self, encryption_key=None):
        # Load encryption key from file or use provided key
        self.encryption_key = encryption_key or self.load_key()
        self.fernet = Fernet(self.encryption_key)

    def load_key(self):
        # Load the encryption key from a file
        try:
            with open("secret.key", "rb") as key_file:
                return key_file.read()
        except FileNotFoundError:
            raise FileNotFoundError("Encryption key file not found! Please generate a key using the generate_key.py script.")

    def encrypt_password(self, password):
        # Encrypt the password and return it as a string
        return self.fernet.encrypt(password.encode()).decode()

    def decrypt_password(self, encrypted_password):
        # Decrypt the password and return it as a string
        return self.fernet.decrypt(encrypted_password.encode()).decode()

    def encrypt_data(self, data):
        return self.fernet.encrypt(data.encode()).decode()

    def decrypt_data(self, encrypted_data):
        # Decrypt the encrypted data and return it as a string
        return self.fernet.decrypt(encrypted_data.encode()).decode()

    def log_event(self, message):
        # Log a provided message to the 'event_log.txt' file
        logging.info(message)

    def toggle_security(self, enable):
        # Print a message to show whether security features are enabled or disabled
        if enable:
            print("Security features are enabled.")
        else:
            print("Security features are disabled.")

    def is_valid_password(self, password):
        # Check if the password meets the required criteria
        if (len(password) < 8 or
            not re.search(r"\d", password) or 
            not re.search(r"[A-Z]", password) or 
            not re.search(r"[a-z]", password) or 
            not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)):
            print("Password must be at least 8 characters long and include an uppercase letter, a lowercase letter, a number, and a special character.")
            return False
        return True