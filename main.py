from auth.auth import login
from utils.helpers import load_json, save_json, prompt_input
import json
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

print("Welcome to the CLI To-Do App")
print("1. Login")
print("2. About")

choice = input("Choose an option: ")

if choice == "1":
    username = input("Username: ")
    password = input("Password: ")
    
    # load users
    users = load_json("data/users.json")
    
    user = next((u for u in users if u['username'] == username), None)
    
    success, message = login(users, username, password)
    print(message)
    
    if success:
        while True:
            print("Welcome to the App")
            print("1. View Task(s)")
            print("2. Add Task")
            print("3. Edit Task")
            print("4. Delete Task")
            print("5. User Management")
            
            choice = input("Choose an option: ")
            
            if choice == "5":
                while True:
                    print("User Management System. Please choose an option.")
                    print("1. Add User")
                    print("2. Edit User")
                    print("3. View User(s)")
                    print("4. Delete User")
                    print("5. Go Back")
                    
                    choice = prompt_input("Choose an option: ")
                    
                    if choice == None:
                        break
                    
                    if choice == "1": #Add User
                        print("You are trying to add a new user. Input the details.")
                        username = prompt_input("Username")
                        if username == None:
                            continue
                        password = prompt_input("Password")
                        if password == None:
                            continue
                        
                        
                        users.append({
                            "username":username,
                            "password":hash_password(password),
                            "is_active":True,
                            })
                        
                        save_json("data/users.json", users)
                        
                        print("You have successfully added a new user!")
                        
                    
            else:
                print("That is an invalid choice. Please try again!")

elif choice == "2":
    print("This app helps you manage tasks with user accounts.")