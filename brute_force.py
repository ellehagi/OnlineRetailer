from security_1 import Security
import time

# Brute force attack function
def brute_force_attack(username, repo, security):
    password_list = ["password123", "admin123", "password", "letmein", "admin"]
    
    # Loop through each password and attempt to login
    for password in password_list:
        print(f"Attempting login with {password}...")

        # Simulate authentication using the provided password
        user = repo['users'].get(username)
        if user and security.decrypt_password(user['password']) == password:
            print(f"Password found: {password}")
            return True
        else:
            print("Incorrect password.")

        
        time.sleep(1)  

    print("Brute force attack failed.")
    return False


# Example repo and security setup for testing
if __name__ == "__main__":
    # Initialize Security with the fixed key
    security = Security(encryption_key=b'your-actual-encryption-key-here')

    
    repo = {
        'users': {
            'admin': {
                'password': 'YCDI7ZABbnJlstAZ14pB7YYDPKQIrkx1zvxkGQXZQn4='  
            }
        }
    }

    
    brute_force_attack('admin', repo, security)