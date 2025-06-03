from utils.helpers import hash_password

def login(users, username, password):
    user = next((u for u in users if u['username'] == username), None)
    
    if not user:
        return False, print("User not found.")
    elif not user["is_active"]:
        return False, print("Account is disabled.")
    elif hash_password(password) == user["password"]:
        return True, print(f"Welcome, {username}!")
    else:
        return False, print("Incorrect Password")