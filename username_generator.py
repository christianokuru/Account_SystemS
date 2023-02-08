

import random
import string
import json
import argon2
import secrets
import forgotpass

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.email_provider = self.get_email_provider()
        self.email = f'{first_name}{last_name}@{self.email_provider}'
        self.password = self.generate_password()
        self.hashed_password = self.hash_password(self.password)
        
    def generate_password(self, length=16):
        password_chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(password_chars) for i in range(length))
    
    def green_text(self, text):
        return f'\033[32m{text}\033[0m'
    
    def get_email_provider(self):
        providers = ['gmail.com', 'yahoo.com', 'hotmail.com']
        print("Enter 'c' for custom email provider or choose from the following list:")
        for i, provider in enumerate(providers):
            print(f'{i+1}: {provider}')
        choice = input("Your choice: ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(providers):
                return providers[choice-1]
        elif choice == 'c':
            return input("Enter custom email provider: ")
        else:
            print("Invalid choice, using default provider (gmail.com)")
            return 'gmail.com'
    
    def hash_password(self, password):
        salt = secrets.token_bytes()
        return argon2.argon2_hash(password, salt=salt).hex()
    
    def save_to_file(self):
      with open('details.json', 'a') as f:
          user_data = {
              'first_name': self.first_name,
              'last_name': self.last_name,
              'email': self.email,
              'password': self.hashed_password
          }
          json.dump(user_data, f)
          f.write('\n')
          
    def forgot_password(self):
        new_password = self.generate_password()
        new_hashed_password = self.hash_password(new_password)
        self.hashed_password = new_hashed_password
        self.save_to_file()
        return new_password


def create_user():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    user = User(first_name, last_name)
            
    email = user.green_text(f'Generated email: {user.email}')
    password = user.green_text(f'Generated password: {user.password}')
            
    print(email)
    print(password)
    user.save_to_file()

#===========================================================
print('Hello, there... Welcome!')
print()
print('What do you want to do?\n1... Create new User\n2... Forgot Password')
print()


choice = int(input('Your Choice: '))

if choice == 1:
    create_user()
elif choice == 2:
    reset = input('Do you really want to reset your password? (y/n) ')
    if reset == 'y':
        forgotpass.reset_password()
    else:
        print('Bye Bitch!!')
else:
    print('Invalid Input')   




    


