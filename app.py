from database.database_manager import create_database
from services.search_service import smart_search

create_database()

while True:

    print("\n==============================")
    print("        ChemAI v1.0")
    print("==============================")
    print("1. Search Compound")
    print("2. Exit")

    choice = input("\nChoose : ")

    if choice == "1":

        smart_search()

    elif choice == "2":

        print("\nGoodbye!")
        break

    else:

        print("\nInvalid Choice!")
