from database.database_manager import initialize_database
from services.search_service import search_compound_menu
from services.similarity_service import similarity_search_menu


def show_banner():
    print("=" * 50)
    print("             ChemAI v2.0")
    print("=" * 50)


def show_menu():
    print("\n1. Search Compound")
    print("2. Similarity Search")
    print("3. Exit")


def main():

    initialize_database()

    while True:

        show_banner()
        show_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":
            search_compound_menu()

        elif choice == "2":
            similarity_search_menu()

        elif choice == "3":
            print("\nThank you for using ChemAI!")
            break

        else:
            print("\nInvalid Choice!\n")


if __name__ == "__main__":
    main()