# # Computer-Based Testing (CBT) program

def ask_question(question, options, correct_answer):
    print(question)
    for option in options:
        print(option)
    answer = input("\nEnter an option from a to d: ").lower()
    
    if answer == correct_answer:
        return 1  
    else:
        return 0   

def run_quiz():
    print("Welcome to the CBT Exam!\n")
    
    score = 0  

    questions = [
        {
            "question": "1. What is 2 + 2?",
            "options": ["a) 3", "b) 4", "c) 5", "d) 6"],
            "answer": "b"
        },
        {
            "question": "2. What color is the sky on a clear day?",
            "options": ["a) Red", "b) Blue", "c) Green", "d) Yellow"],
            "answer": "b"
        },
        {
            "question": "3. How many legs does a spider have?",
            "options": ["a) 6", "b) 7", "c) 8", "d) 9"],
            "answer": "c"
        },
        {
            "question": "4. What sound does a cow make?",
            "options": ["a) Meow", "b) Bark", "c) Moo", "d) Quack"],
            "answer": "c"
        },
        {
            "question": "5. What is the opposite of 'hot'?",
            "options": ["a) Warm", "b) Cold", "c) Cool", "d) Boiling"],
            "answer": "b"
        }
    ]

    for q in questions:
        print()
        score += ask_question(q["question"], q["options"], q["answer"])


    print("\nAt the end of the CBT exam, you scored", score, "points.")

run_quiz()


# Phonebook

phone_book = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    favorite = False  
    contact = {"name": name, "phone": phone, "favorite": favorite}
    phone_book.append(contact)
    print("Contact added successfully!\n")

def view_contacts():
    if not phone_book:
        print("Phone book is empty.\n")
        return
    print("\nContacts:")
    for contact in phone_book:
        fav_status = "❤️" if contact["favorite"] else ""
        print(f"Name: {contact['name']}, Phone: {contact['phone']} {fav_status}")
    print()


def update_contact(phone_number):
    for contact in phone_book:
        if contact["phone"] == phone_number:
            print("Updating contact...")
            new_name = input("Enter new name: ")
            new_phone = input("Enter new phone number: ")
            contact["name"] = new_name
            contact["phone"] = new_phone
            print("Contact updated successfully!\n")
            return
    print("Contact not found.\n")

def delete_contact(phone_number):
    for contact in phone_book:
        if contact["phone"] == phone_number:
            phone_book.remove(contact)
            print("Contact deleted successfully!\n")
            return
    print("Contact not found.\n")

def search_contact(name):
    for contact in phone_book:
        if contact["name"].lower() == name.lower():
            fav_status = "❤️" if contact["favorite"] else ""
            print(f"Found -> Name: {contact['name']}, Phone: {contact['phone']} {fav_status}\n")
            return
    print("Contact not found.\n")

def mark_favorite(phone_number):
    for contact in phone_book:
        if contact["phone"] == phone_number:
            contact["favorite"] = True
            print("Contact marked as favorite!\n")
            return
    print("Contact not found.\n")

def unmark_favorite(phone_number):
    for contact in phone_book:
        if contact["phone"] == phone_number:
            contact["favorite"] = False
            print("Contact unmarked as favorite!\n")
            return
    print("Contact not found.\n")

def main():
    while True:
        print("Phone Book Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contact")
        print("6. Mark Favorite")
        print("7. Unmark Favorite")
        print("8. Exit")
        
        choice = input("Choose an option (1-8): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            phone = input("Enter phone number to update: ")
            update_contact(phone)
        elif choice == "4":
            phone = input("Enter phone number to delete: ")
            delete_contact(phone)
        elif choice == "5":
            name = input("Enter name to search: ")
            search_contact(name)
        elif choice == "6":
            phone = input("Enter phone number to mark as favorite: ")
            mark_favorite(phone)
        elif choice == "7":
            phone = input("Enter phone number to unmark as favorite: ")
            unmark_favorite(phone)
        elif choice == "8":
            print("Exiting Phone Book. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
