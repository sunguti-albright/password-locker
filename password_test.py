# import unittest
# import pyperclip
# from password import User
# from password import Credentials

# class PasswordTest(unittest.TestCase):
#     '''
#     Test class that defines test cases for the password class behaviours.
#     Args:
#         unittest.TestCase: TestCase class that helps in creating test cases
#     '''
#     def setUp(self):
#         '''
#         Set up method to run before each test cases.
#         '''
#         self.new_user = User("Albright", "user")
#         self.new_credential = Credentials("Albright", "user", "12345")

#     def test_init(self):
#         '''
#         test_init test case to test if the object is initialized properly
#         '''
#         self.assertEqual(self.new_user.user_name, "Albright")
#         self.assertEqual(self.new_user.password, "user")
#         self.assertEqual(self.new_credential.user_name, "Albright")
#         self.assertEqual(self.new_credential.account_name, "user")
#         self.assertEqual(self.new_credential.password, "12345")

#     def test_save_user(self):
#         '''
#         test_save_user test case to test if the user object is saved into
#         the user list
#         '''
#         self.new_user.save_user()
#         self.assertEqual(len(User.user_list), 1)

#     def test_save_multiple_user(self):
#         '''
#         test_save_multiple_user to check if we can save multiple user
#         objects to our user_list
#         '''
#         self.new_user.save_user()
#         test_user = User("Test", "user")
#         test_user.save_user()
#         self.assertEqual(len(User.user_list), 2)

#     def test_delete_user(self):
#         '''
#         test_delete_user to test if we can remove a user from our user list
#         '''
#         self.new_user.save_user()
#         test_user = User("Test", "user")
#         test_user.save_user()

#         self.new_user


