from database.database_manager import initialize_database
from services.search_service import search_compound_menu


def show_banner():
    print("=" * 50)
    print("             ChemAI v2.0")
    print("=" * 50)


def show_menu():
    print("\n1. Search Compound")
    print("2. Exit")


def main():

    initialize_database()

    while True:

        show_banner()
        show_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":
            search_compound_menu()

        elif choice == "2":
            print("\nThank you for using ChemAI!")
            break

        else:
            print("\nInvalid Choice!\n")


if name == "main":
    main()
