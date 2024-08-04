import re
users = {}

def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

def register():
    print("Register")
    username = input("Enter username: ")
    
    if username in users:
        print("Username already exists. Please try a different one.")
        return
    
    while True:
        print("Password must be at least 8 characters long. Password must contain uppercase and lowercase characters, digits and special characters.")
        password = input("Enter password: ")
        
        if validate_password(password):
            users[username] = password
            print(password)
            print("Registration successful!")
            break
        
def login():
    print("Login")
    username = input("Enter username: ")
    if username not in users:
        print("Username not found. Please register first.")
        return
    
    password = input("Enter password: ")
    if users[username] == password:
        print("Login successful!")
    else:
        print("Incorrect password. Please try again.")

def main():
    print("Welcome to the System")
    while True:
        print("\n1. Register")
        print("\n2. Login")
        choice = input("Enter choice (1/2): ")
        
        if choice == '1':
            register()
        elif choice == '2':
            login()
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
