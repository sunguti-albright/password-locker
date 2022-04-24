import unittest
from password import User

class PasswordTest(unittest.TestCase):

    def setUp(self):
        """
        method to run before each test case
        """
        self.new_user = User ("Albright", "yeswecan")

    def test_password_init(self):
        '''
        test_password_init to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.user_name, "Albright")
        self.assertEqual(self.new_user.password, "yeswecan")
if __name__ == '__main__':
    unittest.main()