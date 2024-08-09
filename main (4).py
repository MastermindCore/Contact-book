# Simple Contact Book in Python

contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    contacts[name] = {'phone': phone, 'email': email}
    print(f"Contact {name} added successfully.\n")

def view_contacts():
    if contacts:
        print("\n--- Contact List ---")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
        print("\n")
    else:
        print("No contacts available.\n")

def search_contact():
    name = input("Enter the name of the contact to search: ")
    if name in contacts:
        print(f"\nContact found - Name: {name}, Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}\n")
    else:
        print(f"No contact found with the name {name}.\n")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.\n")
    else:
        print(f"No contact found with the name {name}.\n")

def menu():
    while True:
        print("Contact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    menu()
