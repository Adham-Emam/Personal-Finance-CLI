import os
import json
import re
import bcrypt
import getpass
import tempfile
from utils.currencies import currencies


class Authenticator:
    def __init__(self, users_file="database/users.json"):
        self.users_file = users_file
        os.makedirs(os.path.dirname(self.users_file), exist_ok=True)
        # ensure file exists
        if not os.path.exists(self.users_file):
            with open(self.users_file, "w") as f:
                f.write("{}")

    # ---------- Utilities ----------
    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def load_users(self):
        try:
            with open(self.users_file, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return {}

    def save_users(self, users):
        # atomic write
        dirpath = os.path.dirname(self.users_file)
        fd, tmp_path = tempfile.mkstemp(dir=dirpath)
        try:
            with os.fdopen(fd, "w") as tmp:
                json.dump(users, tmp, indent=2)
            os.replace(tmp_path, self.users_file)
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    def hash_password(self, password: str) -> str:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    def verify_password(self, password: str, hashed: str) -> bool:
        try:
            return bcrypt.checkpw(password.encode(), hashed.encode())
        except Exception:
            return False

    # ---------- Validation ----------
    def validate_username(self, username: str) -> bool:
        return bool(re.fullmatch(r"[A-Za-z0-9_]{3,30}", username))

    def validate_email(self, email: str) -> bool:
        # simple regex, sufficient for CLI validation
        return bool(re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email.strip().lower()))

    def validate_password(self, password: str) -> bool:
        return len(password) >= 8

    # ---------- Profile ----------
    def first_time_profile(self, username: str):
        # use the class utility to clear the screen
        self.clear_screen()

        users = self.load_users()
        user = users.get(username, {})

        # if profile already completed in users.json and profile file exists, do nothing
        profile_dir = os.path.join("database", username)
        profile_path = os.path.join(profile_dir, "profile.json")
        if (
            user.get("first_name")
            and user.get("last_name")
            and user.get("currency")
            and os.path.exists(profile_path)
        ):
            return

        print("Complete your profile (first time login)")
        # add verfication for firstName and lastName
        first_name = input("First name: ").strip()
        last_name = input("Last name: ").strip()

        while True:
            currency = (
                input("Currency (USD, EUR, etc): ").upper().strip() or "USD"
            )  # default currency USD
            if currency and currency in currencies:
                break
            else:
                print("Invalid currency. Try again.")

        # update users.json entry
        user["first_name"] = first_name
        user["last_name"] = last_name
        user["currency"] = currency
        users[username] = user
        self.save_users(users)

        # ensure user folder exists and write profile.json atomically
        os.makedirs(profile_dir, exist_ok=True)
        profile_data = {
            "first_name": first_name,
            "last_name": last_name,
            "email": user.get("email", ""),
        }

        fd, tmp_path = tempfile.mkstemp(dir=profile_dir)
        try:
            with os.fdopen(fd, "w") as tmp:
                json.dump(profile_data, tmp, indent=2)
            os.replace(tmp_path, profile_path)
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

        print(f"Profile saved to {profile_path}.")

    # ---------- Register ----------
    def register(self):
        self.clear_screen()
        users = self.load_users()

        print("Register a new account")
        while True:
            username = input("Username (3-30, letters/numbers/_): ").strip()
            if not self.validate_username(username):
                print("Invalid username format.")
                continue
            if username in users:
                print("Username already exists.")
                continue
            break

        while True:
            email = input("Email: ").strip().lower()
            if not self.validate_email(email):
                print("Invalid email format.")
                continue
            # check unique email
            if any(u.get("email", "").lower() == email for u in users.values()):
                print("Email already in use.")
                continue
            break

        while True:
            password = getpass.getpass("Password (min 8 chars): ")
            if not self.validate_password(password):
                print("Password too short.")
                continue
            confirm = getpass.getpass("Confirm password: ")
            if password != confirm:
                print("Passwords do not match.")
                continue
            break

        hashed = self.hash_password(password)
        users[username] = {
            "email": email,
            "password": hashed,
            "first_name": "",
            "last_name": "",
        }
        self.save_users(users)
        print("✅ Registration successful. Please login to continue.")
        return username

    # ---------- Login ----------
    def login(self, max_attempts: int = 3):
        self.clear_screen()
        users = self.load_users()
        print("Login (use username or email)")
        attempts = 0
        while attempts < max_attempts:
            identifier = input("Username or email: ").strip()
            password = getpass.getpass("Password: ")
            # find by username or email
            found_username = None
            if identifier in users:
                found_username = identifier
            else:
                for uname, meta in users.items():
                    if meta.get("email", "").lower() == identifier.lower():
                        found_username = uname
                        break
            if not found_username:
                print("No such user. Try again.")
                attempts += 1
                continue
            user_meta = users.get(found_username, {})
            if self.verify_password(password, user_meta.get("password", "")):
                print("✅ Login successful.")
                # ensure profile completed
                if not user_meta.get("first_name") or not user_meta.get("last_name"):
                    self.first_time_profile(found_username)
                return found_username
            else:
                print("Incorrect password.")
                attempts += 1

        print("Maximum login attempts reached.")
        return None

    # ---------- Combined flow ----------
    def run(self):
        """
        Presents a small menu: login / register / exit
        Returns authenticated username or None
        """
        while True:
            self.clear_screen()
            print("1) Login")
            print("2) Register")
            print("0) Exit")
            choice = input("Choose: ").strip()
            if choice == "1":
                user = self.login()
                if user:
                    return user
            elif choice == "2":
                self.register()
                input("Press Enter to continue to login...")
            elif choice == "0":
                return None
            else:
                print("Invalid choice.")
                input("Press Enter to continue...")
