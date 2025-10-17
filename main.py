import pyfiglet
import os
from function.main_menu import MainMenu


def main():
    os.system("cls" if os.name == "nt" else "clear")

    ascii_art = pyfiglet.figlet_format("Welcome Back!", font="slant")
    print(ascii_art)

    username = input("Enter your name: ")
    main_menu = MainMenu(username)
    main_menu.run()


if __name__ == "__main__":
    main()
