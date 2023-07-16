from .login import login
from .register import register


def main():
    while True:
        print("1) Login")
        print("2) Register")
        print("3) Exit")
        choice = input("> ")

        if choice == "1":
            login()

        elif choice == "2":
            register()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()