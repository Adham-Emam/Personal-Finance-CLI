import os
from function.menu_navigator import MenuNavigator


class Settings:
    def __init__(self, username):
        self.username = username
        self.menu = {
            "1": "📝 Edit Profile",
            "2": "🔑 Change Password",
            "3": "🗑️ Reset All Data",
            "4": "🔙 Back to Main Menu",
            "0": "🚪 Exit",
        }
        self.db_path = f"database/{username}"
        self.menu_navigator = MenuNavigator(self.menu)

    def run(self):
        os.system("cls" if os.name == "nt" else "clear")
        while True:
            self.menu_navigator.print_menu()
            choice = self.menu_navigator.choice()
            if choice == "0":
                self.menu_navigator.exit()
                return
            if choice == "4":
                return

            self.menu_navigator.handle_choice(choice)

    def handle_choice(self, choice):
        match choice:
            case "1":
                print("Edit Profile")
            case "2":
                print("Change Password")
            case "3":
                print("Reset All Data")

    def edit_profile(self, username):
        pass

    def change_password(self, username):
        pass

    def reset_all_data(self, username):
        pass
