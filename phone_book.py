contacts = [
    {"name": "Jeffrey Benson", "phone_number": "09034478902", "is_favorite": True},
    {"name": "Sam Oladapo", "phone_number": "08032417902", "is_favorite": False},
]

def _pretty_print_contact(contact: dict[str, str]):
    return f"Contact Name: {contact["name"]} --- Phone Number: {contact["phone_number"]}{' ⭐' if contact['is_favorite'] else ''}"

def add_contact():
    name = input("Enter the new contact's name: ").strip()
    phone_number = input("Enter the new contact's phone number: ").strip()
    new_contact = {"name": name, "phone_number": phone_number, "is_favorite": False}
    contacts.append(new_contact)
    pretty_contact = _pretty_print_contact(new_contact)
    print(f"{pretty_contact} added successfully")


def view_contacts():
    for contact in contacts:
        print(_pretty_print_contact(contact))

# 1. Go through the contacts
# 2. Check if the phone_number in each contact is the same as the one entered by the user


def update_contact(phone_number):
    for contact in contacts:
        if contact['phone_number'] == phone_number:

            # name = input(f"Enter the new name or leave blank to use '{contact['name']}': ").strip()
            # _phone_number = input(f"Enter the new phone number or leave blank to use '{contact["phone_number"]}': ").strip()

            # if name:
            #     contact['name'] = name
            # if _phone_number:
            #     contact['phone_number'] = _phone_number

            name = input(f"Enter the new name or leave blank to use '{contact['name']}': ").strip() or contact['name']
            _phone_number = input(f"Enter the new phone number or leave blank to use '{contact["phone_number"]}': ").strip() or contact['phone_number']

            original_contact = contact.copy()

            contact['name'] = name
            contact['phone_number'] = _phone_number
            print(f"{_pretty_print_contact(original_contact)} updated to {_pretty_print_contact(contact)}")
            return
        
    print("Contact not found")
    return

def delete_contact(phone_number):
    for contact in contacts:
        if contact['phone_number'] == phone_number:
            contacts.remove(contact)
            print(f"{_pretty_print_contact(contact)} deleted successfully")
            return
        
    print("Contact not found")
    return

def search_contact(name: str):
    for contact in contacts:
        # if contact['name'] == name:  # exact
        if name.lower() in contact['name'].lower():
            print("Contact found")
            print(f"{_pretty_print_contact(contact)}")
            return
        
    print("Contact not found")
    return


def _toggle_favorite(favorite_status, phone_number):
    for contact in contacts:
        if contact['phone_number'] == phone_number:
            contact['is_favorite'] = favorite_status
            print(f"{_pretty_print_contact(contact)} is {'now' if favorite_status else 'not'} a favorite")
            return
    print("Contact not found")
    return


def mark_as_favorite(phone_number):
    return _toggle_favorite(True, phone_number)

def unmark_as_favorite(phone_number):
    return _toggle_favorite(False, phone_number)



menu = """Menu
AC. Add Contact
VC. View Contact
UC. Update Contact
DC. Delete Contact
SC. Search Contact
MCF. Mark Contact as Favorite
UCF. Unmark Contact as Favorite
Q. Quit
"""

while True:
    print(menu)
    choice = input("Choose an option from the menu above: ").strip().lower()

    if choice == "ac":
        add_contact()
    elif choice == "vc":
        view_contacts()
    elif choice == 'uc':
        phone_number = input("Enter the phone number of the contact you wish to update: ").strip()
        update_contact(phone_number)
    elif choice == 'dc':
        phone_number = input("Enter the phone number of the contact you wish to delete: ").strip()
        delete_contact(phone_number)
    elif choice == 'sc':
        name = input("Enter the name of the contact to search for: ").strip()
        search_contact(name)
    elif choice == 'mcf':
        phone_number = input("Enter the phone number of the contact you wish to mark as favorite: ").strip()
        mark_as_favorite(phone_number)
    elif choice == 'ucf':
        phone_number = input("Enter the phone number of the contact you wish to unmark as favorite: ").strip()
        unmark_as_favorite(phone_number)
    elif choice == "q":
        break
    else:
        print("Invalid choice")


