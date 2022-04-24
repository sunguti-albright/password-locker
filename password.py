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
    @classmethod
    def find_by_name(name, password):
        """Finds the user by name"""
        find_user = ""
        for user in User.user_list:
            if user.user_name == name and user.password == password:
                find_user = user.username
        return find_user
