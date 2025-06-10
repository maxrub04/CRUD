import re
import json
import User_Manager as User

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
            User.create_user()
        elif choice == '2':
            User.view_user()
        elif choice == '3':
            User.update_user()
        elif choice == '4':
            User.delete_user()
        elif choice == '5':
            User.list_users()
        elif choice == '0':
            break
        else:
            print("Error. Try again")