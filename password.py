import pyperclip
import random
import string

class User:
    """
    Initiates new instances of a user
    """
    
    user_list = []

    def __init__(self, user_name, password):
        """
        Initializes the user
        """
        self.user_name = user_name
        self.password = password
        
    def save_user(self):
        """Saves the user"""
        User.user_list.append(self)

    @classmethod
    def display_user(cls):
        """Displays the user"""
        return cls.user_list
    def delete_user(self):
        """Deletes the user"""
        User.user_list.remove(self)
  
    def user_check_me(username, password):
        """
        user_check_me method to check if a certain user is in user_list or not
        """
        check_me = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                    check_me == user.username
        return check_me
    #The End!
#The End of User Class!
class Credentials:
    '''
    Credentials class to create new objects of Credentials
    '''
#     credentials_list = []
#     # Empty object to hold new credentials

#     def __init__(self,platform,email,password):
#         '''
#         __init__ Method to define credentials properties
#         '''
#         self.platform = platform
#         self.email = email
#         self.password = password
#     #The End!

#     def save_credentials(self):
#         '''
#         save_credentials class to save and store new credentials into credentials_list
#         '''
#         Credentials.credentials_list.append(self)
#     #The end!
    
#     def delete_credentials(self):
#         '''
#         delete_credentials class to remove credential ffrom credentials_list
#         '''
#         Credentials.credentials_list.remove(self)
#     #The end!

#     @classmethod
#     def find_credentials(cls, platform):
#         '''
#         find_credentials class to find credentials and display their information
#         '''
#         for crede in cls.credentials_list:
#             if crede.platform == platform:
#                 return crede
#     #The end!

#     @classmethod
#     def credential_exists(cls, platform):
#         '''
#         credential_exists class to check if credentials already exists
#         '''
#         for crede in cls.credentials_list:
#             if crede.platform == platform:
#                 return True
#         return False
#     #The end!

#     @classmethod
#     def display_credentials(cls):
#         '''
#         display_credentials class to display credentials from credentials_list
#         '''
#         return cls.credentials_list
#     #The end!

#     def new_password(stringLength = 10):
#         '''
#         new_password method to generate a new password
#         '''
#         password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
#         return ''.join(random.choice(password) for i in range(stringLength))
#     #The end!

#     @classmethod
#     def copy_credentials(cls,platform):
#         '''
#         copy_credentials class to be able to copy credentials to the clipboard
#         '''
#         found_credentials = Credentials.find_credentials('Gmail')
#         pyperclip.copy(found_credentials.platform)
#     #The end!
# #The End of Credentials class


    
