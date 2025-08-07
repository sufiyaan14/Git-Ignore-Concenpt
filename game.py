import os

FILENAME = "contacts.txt"

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    with open(FILENAME, "a") as file:
        file.write(f"{name},{phone},{email}\n")
    print("✅ Contact added successfully!")

def view_contacts():
    if not os.path.exists(FILENAME):
        print("No contacts found.")
        return
    with open(FILENAME, "r") as file:
        contacts = file.readlines()
        print("\n--- All Contacts ---")
        for i, contact in enumerate(contacts, start=1):
            name, phone, email = contact.strip().split(",")
            print(f"{i}. Name: {name} | Phone: {phone} | Email: {email}")
        print("---------------------")

def search_contact():
    search_name = input("Enter name to search: ").lower()
    found = False
    with open(FILENAME, "r") as file:
        for contact in file:
            name, phone, email = contact.strip().split(",")
            if search_name in name.lower():
                print(f"Found: Name: {name}, Phone: {phone}, Email: {email}")
                found = True
    if not found:
        print("No contact found with that name.")

def delete_contact():
    delete_name = input("Enter name to delete: ").lower()
    updated_contacts = []
    deleted = False

    with open(FILENAME, "r") as file:
        for contact in file:
            name, phone, email = contact.strip().split(",")
            if delete_name != name.lower():
                updated_contacts.append(contact)
            else:
                deleted = True

    with open(FILENAME, "w") as file:
        file.writelines(updated_contacts)

    if deleted:
        print("✅ Contact deleted.")
    else:
        print("❌ No contact found with that name.")

def main():
    while True:
        print("\n===== Contact Book =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("📕 Exiting Contact Book. Bye!")
            break
        else:
            print("Invalid choice. Please try again and again.")

if __name__ == "__main__":
    main()
