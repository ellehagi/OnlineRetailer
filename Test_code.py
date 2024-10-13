import unittest
from unittest.mock import MagicMock
from user import UserManager, User  
from security_1 import Security  

class TestUserManager(unittest.TestCase):

    def setUp(self):
        self.users = {}
        self.security = MagicMock(spec=Security)
        self.user_manager = UserManager(self.users, self.security)
        self.user_manager.save_users = MagicMock()

    def test_create_user(self):
        # Test creating a user
        self.security.is_valid_password.return_value = True
        self.security.encrypt_password.return_value = "encrypted_password"
        
        self.user_manager.create_user("testuser", "TestPassword123")
        self.assertIn("testuser", self.users)
        self.assertEqual(self.users["testuser"]["password"], "encrypted_password")

    def test_authenticate_user(self):
        # Test user authentication
        self.security.decrypt_password.return_value = "TestPassword123"
        self.user_manager.create_user("validuser", "TestPassword123")
        
        user = self.user_manager.authenticate("validuser", "TestPassword123")
        self.assertIsNotNone(user)
        self.assertEqual(user.username, "validuser")

    def test_delete_user(self):
        # Test deleting a user
        self.user_manager.create_user("deletableuser", "password")
        self.user_manager.delete_user("deletableuser")
        self.assertNotIn("deletableuser", self.users)

    def test_update_user(self):
        # Test updating a user's password
        self.security.is_valid_password.return_value = True
        self.security.encrypt_password.return_value = "new_encrypted_password"
        
        self.user_manager.create_user("updateuser", "OldPassword")
        self.user_manager.update_user("updateuser", "NewPassword")
        self.assertEqual(self.users["updateuser"]["password"], "new_encrypted_password")


class TestSecurity(unittest.TestCase):

    def setUp(self):
        # Initialise Security object with a generated key
        self.security = Security()

    def test_encrypt_decrypt_password(self):
        # Testing encryption and decryption of a password
        password = "SecurePassword123!"
        encrypted_password = self.security.encrypt_password(password)
        decrypted_password = self.security.decrypt_password(encrypted_password)
        self.assertEqual(password, decrypted_password)

    def test_is_valid_password(self):
        # Test password validation with various valid and invalid passwords
        valid_password = "StrongPass1!"
        self.assertTrue(self.security.is_valid_password(valid_password))

        short_password = "Shor1!"
        self.assertFalse(self.security.is_valid_password(short_password))

        no_number_password = "NoNumber!"
        self.assertFalse(self.security.is_valid_password(no_number_password))

        no_uppercase_password = "nouppercase1!"
        self.assertFalse(self.security.is_valid_password(no_uppercase_password))

        no_special_char_password = "NoSpecial1"
        self.assertFalse(self.security.is_valid_password(no_special_char_password))

    def test_log_event(self):
        # Test if events are logged correctly
        event_message = "User login attempt"
        self.security.log_event(event_message)
        # Check if the text is written to the log file
        with open("event_log.txt", "r") as log_file:
            log_contents = log_file.read()
        self.assertIn(event_message, log_contents)

    def test_toggle_security(self):
        # Test toggling security off
        self.security.toggle_security(False)
        # Test toggling security on
        self.security.toggle_security(True)


class TestUser(unittest.TestCase):

    def test_user_creation(self):
        # Test User class creation
        user = User("testuser", "TestPassword123")
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.password, "TestPassword123")


if __name__ == '__main__':
    unittest.main()