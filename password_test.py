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

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
        
if __name__ == '__main__':
    unittest.main()