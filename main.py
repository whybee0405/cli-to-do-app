from auth.auth import login
from utils.helpers import load_json, save_json, prompt_input
from auth.user_manager import add_user, edit_user, view_users, delete_user
import json
import hashlib
from tabulate import tabulate

message_invalid_choice = "That is an invalid choice. Try again!"

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
        # Main Home Menu
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
                    
                    if choice == "1": #ADD USER
                        print("You are trying to add a new user. Input the details.")
                        username = prompt_input("Username")
                        if username == None:
                            continue
                        password = prompt_input("Password")
                        if password == None:
                            continue
                        add_user(users, username, password, is_active=True)
                    
                    elif choice == "2": #EDIT USER
                        print("EDIT USER")
                        print(view_users(users))
                        
                        selected_user = prompt_input("Type the username of the user you want to edit: ")
                        
                        user = next((u for u in users if u["username"] == selected_user), None)
                        
                        if user:
                            print(f"You have selected user '{user["username"]}'")
                            print("1. username")
                            print("2. password")
                            print("3. is_active")
                            
                            choice = prompt_input("What do you want to edit? Type a number")
                            match choice:
                                case "1":
                                    # change username
                                    new_username = prompt_input("Type in the new username: ")
                                    print(edit_user(users, user, choice, new_username))
                                    
                                case "2":
                                    # change password
                                    new_password = prompt_input("Type in the new password: ")
                                    print(edit_user(users, user, choice, new_password))
                                    
                                case "3":
                                    # change is_active
                                    print("1. Activate user")
                                    print("2. Deactivate user")
                                    new_status = prompt_input("Choose an option: ")
                                    if new_status == "1" or "2":
                                        print(edit_user(users, user, choice, new_status))
                                    else:
                                        print(message_invalid_choice)
                                        continue
                                    
                                case _:
                                    print(message_invalid_choice)
                                    continue
                        else:
                            print("User not found.")
                    elif choice == "3":
                        # VIEW USERS
                        print(view_users(users))
                        
                    elif choice == "4":
                        # DELETE USER
                        print("DELETE USER")
                        print(view_users(users))
                        
                        selected_user = input("Type username of the user you want to delete: ")
                        confirmation = input("Are you sure you want to delete this user? (y/n)")
                        if confirmation.lower() == "y":
                            print(delete_user(users, selected_user))
                        
                    
            else:
                print(message_invalid_choice)

elif choice == "2":
    print("This app helps you manage tasks with user accounts.")