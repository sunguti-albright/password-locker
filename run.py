#!/usr/bin/env python3.6
from password import User
from password import Credentials # Importing user and credentials classes

def create_user(username,password):
    '''
    create_user method to create a new user
    '''
    new_user = User(username,password)
    return new_user
#The end!

def save_user(user):
    '''
    save_user method to save a user
    '''
    user.save_user()
#The end!

def display_user():
    """
    display_user method to display an existing user
    """
    return User.display_user()
#The end!
def signin_user(username,password):
    """
    signin_user method to check a user and then sign in they exist
    """
    check_user = User.user_check_me(username,password)
    return check_user
#The End!

def create_credential(platform,email,password):
    """
    create_credential method to create new credentials
    """
    new_credential = Credentials(platform,email,password)
    return new_credential
#The end!

def save_credentials(credentials):
    """
    save_credentials method to save credentials in credentials_list
    """
    credentials. save_credentials()
#The end!

def display_credentials():
    """
    display_credentials method to display user's credentials.
    """
    return Credentials.display_credentials()
#The end!

def delete_credential(credentials):
    """
    delete_credential method to delete a credential from credentials list
    """
    credentials.delete_credentials()
#The end!

def find_credential(platform):
    """
    find_credential method to find credentials by the platform name and return the credentials that belong to that platform
    """
    return Credentials.find_credentials(platform)
#The end!

def check_credentials(platform):
    """
    check_credentials method to check if credentials already existed inside that platform and return true or false
    """
    return Credentials.credential_exists(platform)
#The end!

def new_Password():
    '''
    new_password method to generate a new password
    '''
    auto_password = Credentials.new_password()
    return auto_password
#The end!

def copy_credentials(platform):
    """
    copy_credentials class to be able to copy credentials to the clipboard
    """
    return Credentials.copy_credentials(platform)
#The end!

def passwordLocker():
    print(" Hello There:) Welcome to Password Locker...\n Please enter one of the following code to proceed.\n CA ---  Create New Account  \n SI ---  Sign In Your Account  \n")
    
    short_code = input(" ").lower().strip() 
    if short_code == "ca":
        print(" Sign Up")
        print(' *' * 10)
        username = input(" Username: ")
        while True:
            print(" CP - Create your own Password:\n AP - Auto Password")
            password_Choice = input( '_').lower().strip()
            if password_Choice == 'cp':
                password = input(" Enter Password\n")
                break
            elif password_Choice == 'ap':
                password = new_Password()
                break
            else:
                print(" Invalid Password!\n Please try again")
        save_user(create_user(username,password))
        print(" *"*10)
        print(f" Awesome!!!! {username},\n Your account has been created!\n Your password is: {password}")
        print(" *"*10)

    elif short_code == "si":
        print(" *"*10)
        print("Please Enter your Username and your Password to sign in:")
        print(' *' * 10)
        username = input(" Username: ")
        password = input(" Password: ")
        signin = signin_user(username,password)
        if signin_user == signin:
            print(f" Hey {username}.Welcome back!")  
            print('\n')
    
    while True:
        print(" Use these short codes:\n CC - Create a new Credential \n DC - Display Credentials \n FC - Find a Credential \n AP - Auto Password \n DL - Delete credential \n EA - Exit the Application \n")
        short_code = input( '_').lower().strip()
        if short_code == "cc":
            print(" Create New Credential")
            print(" ."*10)
            print(" Platform name ....")
            platform = input( '_').lower()
            print(" Your Platform email")
            email = input( '_')
            while True:
                print(" EP - Enter your password:\n AP - Auto Password")
                password_Choice = input( '_').lower().strip()
                if password_Choice == 'ep':
                    password = input(" Enter Your Own Password\n")
                    break
                elif password_Choice == 'ap':
                    password = new_Password()
                    break
                else:
                    print(" Invalid Password!\n Please try again")
            save_credentials(create_credential(platform,email,password))
            print('\n')
            print(f" Platform Credential for: {platform}")
            print(" *"*10)
            print(f" Email: {email}")
            print(" *"*10)
            print(f" Password:{password}")
            print(" *"*10)
            print(" Has been created succesfully")
            print('\n')
        elif short_code == "dc":
            if display_credentials():
                print(" Here is a list of your credentials: ")
                 
                print(' *' * 10)
                print(' _'* 10)
                for platform in display_credentials():
                    print(f" Platform:{platform.platform} \n Email:{email}\n Password:{password}")
                    print(' _'* 10)
                print(' *' * 10)
            else:
                print("Hmmm...can't seem to find any credentials...")
        elif short_code == "fc":
            print(" What platform do you want to look up?")
            search_name = input( '_').lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f" Platform Name : {search_credential.platform}")
                print(' -' * 10)
                print(f" Email: {search_credential.email} Password :{search_credential.password}")
                print(' -' * 10)
            else:
                print(" That Credential does not exist")
                print('\n')
        elif short_code == "dl":
            print("Input platform name to deelete credentials:")
            search_name = input( '_').lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(" _"*10)
                search_credential.delete_credentials()
                print('\n')
                print(f" Your credentials for : {search_credential.platform}\n Have been deleted!")
                print('\n')
            else:
                print(" That Credential you want to delete does not exist in your list yet")

        elif short_code == 'ap':

            password = new_Password()
            print(f" {password} Has been generated succesfull. You can proceed to use it to your account")
        elif short_code == 'ea':
            print("Sad to see you leave(: Thank you, Come back soon!")
            break
        else:
            print(" Wrong entry... Entry a valid code")
    else:
        print(" Please enter a valid code to continue")


if __name__ == '__main__':
    passwordLocker()

#The End of PASSWORD LOCKER!