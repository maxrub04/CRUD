import re
import json
from User_Manager import UserManager


user_manager = UserManager()
while True:
        print("\n--- User CRUD Menu ---")
        print("1. Create User")
        print("2. View User")
        print("3. Update User")
        print("4. Delete User")
        print("5. List All Users")
        print("0. Exit")

        choice = input("Enter choice (1–6): ")

        if choice == '1':
            user_manager.create_user()
        elif choice == '2':
            user_manager.view_user()
        elif choice == '3':
            user_manager.update_user()
        elif choice == '4':
            user_manager.delete_user()
        elif choice == '5':
            user_manager.show_all_users()
        elif choice == '0':
            break
        else:
            print("Error. Try again")