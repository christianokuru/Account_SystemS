import json

def reset_password():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    
    with open('details.json', 'r') as f:
        for line in f:
            user_data = json.loads(line)
            if user_data['email'] == email:
                user = py2.User(
                    user_data['first_name'],
                    user_data['last_name'],
                    user_data['email'],
                    user_data['password']
                )
                break
        else:
            print("User not found.")
            exit()
    
    forgot_password = input("Did you forget your password? (y/n) ")
    
    if forgot_password == 'y':
        new_password = user.forgot_password()
        print(user.green_text(f'New password: {new_password}'))
    else:
        print(user.green_text(f'Welcome, {user.first_name} {user.last_name}'))

