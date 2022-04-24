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
        
#     def save_user(self):
# #         """Saves the user"""
#         User.user_list.append(self)


