import json
import os

CONTACT_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if not os.path.exists(CONTACT_FILE):
        return []
    with open(CONTACT_FILE, "r") as file:
        return json.load(file)

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACT_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("👤 Enter Name: ").strip()
    phone = input("📞 Enter Phone Number: ").strip()
    email = input("✉️ Enter Email: ").strip()
    address = input("🏠 Enter Address: ").strip()

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("✅ Contact added successfully!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("📭 No contacts found.")
        return

    print("\n📋 Contact List:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")

# Search contacts
def search_contacts(contacts):
    query = input("🔍 Enter name or phone number to search: ").strip().lower()
    found = [c for c in contacts if query in c['name'].lower() or query in c['phone']]
    if not found:
        print("❌ No contact found.")
        return
    print("\n🔎 Search Results:")
    for c in found:
        print(f"\n👤 Name: {c['name']}\n📞 Phone: {c['phone']}\n✉️ Email: {c['email']}\n🏠 Address: {c['address']}")

# Update a contact
def update_contact(contacts):
    name = input("✏️ Enter the name of the contact to update: ").strip().lower()
    for c in contacts:
        if c['name'].lower() == name:
            print(f"\nUpdating contact: {c['name']}")
            c['phone'] = input("📞 New Phone Number: ").strip() or c['phone']
            c['email'] = input("✉️ New Email: ").strip() or c['email']
            c['address'] = input("🏠 New Address: ").strip() or c['address']
            print("✅ Contact updated.")
            return
    print("❗ Contact not found.")

# Delete a contact
def delete_contact(contacts):
    name = input("🗑️ Enter the name of the contact to delete: ").strip().lower()
    for i, c in enumerate(contacts):
        if c['name'].lower() == name:
            confirm = input(f"❓ Are you sure you want to delete {c['name']}? (yes/no): ").lower()
            if confirm == 'yes':
                contacts.pop(i)
                print("🗑️ Contact deleted.")
            else:
                print("❌ Deletion canceled.")
            return
    print("❗ Contact not found.")

# Main menu
def main():
    contacts = load_contacts()

    while True:
        print("\n📒 Contact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("👉 Enter your choice (1-6): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contacts(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            save_contacts(contacts)
            print("💾 Contacts saved. Goodbye!")
            break
        else:
            print("❗ Invalid choice. Please select from 1 to 6.")

if __name__ == "__main__":
    main()
