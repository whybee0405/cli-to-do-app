import hashlib
from utils.helpers import save_json, hash_password
from tabulate import tabulate

def add_user(users, username, password, is_active):

    users.append({
        "username":username,
        "password":hash_password(password),
        "is_active":is_active,
        })
    
    save_json("data/users.json", users)
    
    return "You have successfully added a new user!"
    
def edit_user(users, user, choice, new_data):
    match choice:
        case "1":
            # change username
            for u in users:
                if u["username"] == user["username"]:
                    u["username"] = new_data
                    
            save_json("data/users.json", users)
            
            return f"{user['username']} username has been changed to '{new_data}'"
        
        case "2":
            # change password
            for u in users:
                if u["username"] == user["username"]:
                    u["password"] = hash_password(new_data)
            
            save_json("data/users.json", users)
            
            return f"{user['username']} password has been changed!"
        
        case "3":
            # change is_active
            if new_data == "1":
                for u in users:
                    if u["username"] == user["username"]:
                        u["is_active"] = True
                
                save_json("data/users.json", users)
                        
                return f"{user['username']} is now Activated!"
            
            elif new_data == "2":
                for u in users:
                    if u["username"] == user["username"]:
                        u["is_active"] = False
                        
                save_json("data/users.json", users)
                
                return f"{user['username']} is now Deactivated!"
            
def view_users(users):
    # filter users so that passwords are not shown when tabulating
    headers = ["username", "is_active"]
    filtered_users = [{key: user[key] for key in headers} for user in users]
    
    return(tabulate(filtered_users, headers="keys", tablefmt="grid"))

def delete_user(users, selected_user):
    for i, user in enumerate(users):
        if user["username"] == selected_user:
            del users[i]

    save_json("data/users.json", users)
    return f"User {selected_user} has been deleted!"        