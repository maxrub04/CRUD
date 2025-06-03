import re


class User:

    def __init__(self, username, name, email, phone, age):
        self.username = username
        self.name = name
        self.email = email
        self.phone = phone
        self.age = age

    def to_dict(self):
        return {
            "username": self.username,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "age": self.age
        }

    @staticmethod
    def validate_username(username, existing_users):
        if not username.strip():
            print("Username cannot be empty")
            return False
        if username in existing_users:
            print("Username already exists")
            return False
        return True

    @staticmethod
    def validate_name(name):
        if not name.strip():
            print("Name cannot be empty")

    @staticmethod
    def validate_email(email):
        if not email.strip():
            print("Email cannot be empty")
            return False
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            print("Invalid email address")
            return False

    @staticmethod
    def validate_phone(phone):
        if not phone.strip():
            print("Phone cannot be empty.")

    @staticmethod
    def validate_age(age):
        if not age.strip():
            print("Age cannot be empty.")
        if not age.isdigit():
            print("Age must be a number.")
        if int(age) <= 0:
            print("Age must be greater than 0.")