import unittest # Importing unittest module
from password import User # Importing user class from password module
from password import Credentials #Importing credentials class from password module

class TestUser(unittest.TestCase):
    '''
    TestUser class to define test cases for the user class behaviours
    '''
    def setUp(self):
        '''
        setUp method to run before each test cases
        '''
        self.new_user = User('Albright','yeswecan') # Create user object
    #The end!
    
    def test_init(self):
        '''
        test_init to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username,'Albright')
        self.assertEqual(self.new_user.password,'yeswecan')
    #The End!
    
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
    #The end!
#The End with TestUser class

class TestCredentials(unittest.TestCase):
    '''
    TestCredentials class to define test cases for the credentials class behaviours
    '''
    def setUp(self):
        '''
        setUp method to run before each test cases
        '''
        self.new_credential = Credentials('Twitter','sungutialbright@gmail.com','blahblah')
    #The end!

    def test_init(self):
        '''
        test_init to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.platform,'Twitter')
        self.assertEqual(self.new_credential.email,'sungutialbright@gmail.com')
        self.assertEqual(self.new_credential.password,'blahblah')
    #The end!

    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into the credentials list
        '''
        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
    #The end!

    def tearDown(self):
        '''
        tearDown method to clean up after each test has run
        '''
        Credentials.credentials_list = []
    #The end!

    def test_save_multiple_credentials(self):
        '''
        test_save_many_credentials test case to test if we can save multiple credentials at a time
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials('Instagram','test.user@gmail.com','yesyes')
        test_credential.save_credentials()

        self.assertEqual(len(Credentials.credentials_list),2)
    #The end!

    def test_delete_credentials(self):
        '''
        test_delete_credentials test case to test if we can remove a credential
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials('Instagram','test.user@gmail.com','yesyes')
        test_credential.save_credentials()
        
        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
    #The end!

    def test_find_credentials(self):
        '''
        test_find_credentials test case to test if we can find credentials and display the information
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials('Instagram','test.user@gmail.com','yesyes')
        test_credential.save_credentials()

        found_credentials = Credentials.find_credentials('Gmail')
        self.assertEqual(found_credentials.platform,test_credential.platform)
    #The end!

    def test_credential_exists(self):
        '''
        test_credential_exists test case to test if credentials exists to get True and false otherwise
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials('Instagram','test.user@gmail.com','yesyes')
        test_credential.save_credentials()

        found_credential_exists = Credentials.credential_exists('Gmail')
        self.assertTrue(found_credential_exists)
    #The end!

    def test_display_all_credentials(self):
        '''
        test_display_all_credentials test case to test if all credentials can be displayed
        '''
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)
    #The end!


if __name__ == '__main__':
    unittest.main()