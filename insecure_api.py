import logging

# Simulate Insecure API actions
def run_insecure_api():
    print("Insecure API started. Passwords and MFA tokens are NOT hashed.")
    logging.warning("Insecure API started without encryption.")
    # Simulate additional insecure API functionality