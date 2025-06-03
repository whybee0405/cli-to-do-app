import json

def load_json(path):
    with open(path,"r") as f:
        json_data = json.load(f)
        return json_data
    
def save_json(path,data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
        return print(f"Successfully save JSON file!")
    
def prompt_input(label, cancel_value="0"):
    value = input(f"{label} (type '{cancel_value}' to cancel): ")
    if value == cancel_value:
        return None
    return value