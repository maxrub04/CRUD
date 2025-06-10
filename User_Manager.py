import json
import os
import User_Model as User
import re

class UserManager:
    EMAIL_PATTERN = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    PHONE_PATTERN = re.compile(r"^\+\d{7,15}$")

    def __init__(self, data_file="data.json"):
        self.data_file = data_file
        self.users = {}
        self.load_users()


    def load_users(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                users_list = json.load(f)
            self.users = {user["username"]: User.from_dict(user) for user in users_list}
        else:
            self.users = {}

    def save_users(self):
        users_list = [user.to_dict() for user in self.users.values()]
        with open(self.data_file, "w") as f:
            json.dump(users_list, f, indent=4)

    def create_user(self):
        print("Creating a new user:")
        while True:
            username = input("Enter username: ")
            if not username:
                print("Username cannot be empty.")
            elif username in self.users:
                print("Username already exists.")
            else:
                break
        while True:
            name = input("Enter name: ")
            if not name:
                print("Name cannot be empty.")
            else:
                break
        while True:
            email = input("Enter email: ")
            if not re.match(self.EMAIL_PATTERN, email):
                print("Invalid email format.")
            else:
                break
        while True:
            phone = input("Enter phone (e.g., +12345678901): ")
            if not re.match(self.PHONE_PATTERN, phone):
                print("Invalid phone number. Must start with + followed by 7 to 15 digits.")
            else:
                break
        while True:
            age = input("Enter age: ")
            if not age.isdigit() or int(age) <= 0:
                print("Age must be a positive integer.")
            else:
                age = int(age)
                break
        user = User(username, name, email, phone, age)
        self.users[username] = user
        self.save_users()
        print("User created successfully.")

    def view_user(self):
        username = input("Enter username to view: ")
        if username in self.users:
            user = self.users[username]
            print(f"Username: {user.username}")
            print(f"Name: {user.name}")
            print(f"Email: {user.email}")
            print(f"Phone: {user.phone}")
            print(f"Age: {user.age}")
        else:
            print("User not found.")

    def update_user(self):
        old_username = input("Enter username to update: ")
        if old_username not in self.users:
            print("User not found.")
            return
        user = self.users[old_username]
        print("Which field to update? (username, name, email, phone, age)")
        field = input("Enter field: ").lower()
        if field == "username":
            while True:
                new_username = input("Enter new username: ")
                if not new_username:
                    print("Username cannot be empty.")
                elif new_username in self.users:
                    print("Username already exists.")
                else:
                    break
            del self.users[old_username]
            user.username = new_username
            self.users[new_username] = user
        elif field == "name":
            while True:
                new_name = input("Enter new name: ")
                if not new_name:
                    print("Name cannot be empty.")
                else:
                    user.name = new_name
                    break
        elif field == "email":
            while True:
                new_email = input("Enter new email: ")
                if not re.match(self.EMAIL_PATTERN, new_email):
                    print("Invalid email format.")
                else:
                    user.email = new_email
                    break
        elif field == "phone":
            while True:
                new_phone = input("Enter new phone (e.g., +12345678901): ")
                if not re.match(self.PHONE_PATTERN, new_phone):
                    print("Invalid phone number. Must start with + followed by 7 to 15 digits.")
                else:
                    user.phone = new_phone
                    break
        elif field == "age":
            while True:
                new_age = input("Enter new age: ")
                if not new_age.isdigit() or int(new_age) <= 0:
                    print("Age must be a positive integer.")
                else:
                    user.age = int(new_age)
                    break
        else:
            print("Invalid field.")
            return
        self.save_users()
        print("User updated successfully.")

    def delete_user(self):
        username = input("Enter username to delete: ")
        if username in self.users:
            del self.users[username]
            self.save_users()
            print("User deleted successfully.")
        else:
            print("User not found.")

    def show_all_users(self):
        if not self.users:
            print("No users found.")
        else:
            for username, user in self.users.items():
                print(f"Username: {user.username}, Name: {user.name}, Email: {user.email}, Phone: {user.phone}, Age: {user.age}")