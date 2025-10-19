import pyfiglet
import os
from function.main_menu import MainMenu
from function.auth import Authenticator


def main():
    os.system("cls" if os.name == "nt" else "clear")

    ascii_art = pyfiglet.figlet_format("Welcome Back!", font="slant")
    print(ascii_art)

    auth = Authenticator()
    username = auth.run()
    if username:
        MainMenu(username).run()


if __name__ == "__main__":
    main()
