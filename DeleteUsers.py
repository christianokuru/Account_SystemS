import json

def delete_user(email):
    with open("details.json", "r") as f:
        data = json.load(f)
    updated_data = [d for d in data if d["email"] != email]
    with open("details.json", "w") as f:
        json.dump(updated_data, f)
