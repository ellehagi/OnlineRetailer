from cryptography.fernet import Fernet

# Generate a valid Fernet key
key = Fernet.generate_key()

# Print the generated key
print(f"Your generated Fernet key: {key.decode()}")

# Optionally save the key to a file
with open("secret.key", "wb") as key_file:
    key_file.write(key)