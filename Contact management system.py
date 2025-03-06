import pickle
class Node:
    def __init__(self):
        self.name = ""
        self.phone_number = 0
        self.next = None
        self.prev = None

class ContactBook:
    def __init__(self):
        self.head = None

    def create_node(self):
        newer = Node()
        newer.name = input("Name of Contact: ")
        newer.phone_number = int(input("Phone Number: "))
        newer.next = None
        newer.prev = None
        if self.head is None:
            self.head = newer
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newer
            newer.prev = temp
        print("Contact Added")

    def display(self):
        temp = self.head
        count = 0
        if temp is None:
            print("No Contacts... Please Add Some Contacts")
        else:
            self.bubble_sort()
            print("Contacts:")
            while temp is not None:
                count += 1
                print(count, ". Name:", temp.name, ", Phone Number:", temp.phone_number)
                temp = temp.next
            print("Total contacts:", count)

    def delete_contact_by_name(self, name_to_delete):
        if self.head is None:
            print("Contact book is already empty.")
            return

        current = self.head
        previous = None

        while current is not None:
            if current.name == name_to_delete:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                    if current.next is not None:
                        current.next.prev = previous
                print("Contact", name_to_delete, "deleted successfully.")
                return
            previous = current
            current = current.next

        print("Contact", name_to_delete, "not found in the contact book.")

    def delete_all_contacts(self):
        temp = self.head
        while temp is not None:
            next_node = temp.next
            del temp
            temp = next_node
        self.head = None
        print("Successfully Deleted All Contacts")

    def delete_contact_by_search(self):
         name_to_search = input("Enter the Name to Delete: ")
         current = self.head
         previous = None
         while current is not None:
            if current.name == name_to_search:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                    if current.next is not None:
                        current.next.prev = previous
                print("Contact", name_to_search, "deleted successfully.")
                return
            previous = current
            current = current.next

         print("Contact", name_to_search, "not found in the contact book.")

    def edit_contacts(self):
        name_to_edit = input("Enter the Name to Edit: ")
        current = self.head
        while current is not None:
            if current.name == name_to_edit:
                print("Name:", current.name)
                print("Phone Number:", current.phone_number)
                new_name = input("Enter New Name: ")
                new_number = int(input("Enter New Number: "))
                current.name = new_name
                current.phone_number = new_number
                print("Contact Edited Successfully")
                return
            current = current.next

        print("Contact", name_to_edit, "not found in the contact book.")

    def search(self):
         name_to_search = input("Enter the Name to Search: ")
         current = self.head
         while current is not None:
            if current.name == name_to_search:
                print("Name:", current.name)
                print("Phone Number:", current.phone_number)
                return
            current = current.next

         print("Contact", name_to_search, "not found in the contact book.")

    def bubble_sort(self):
         if self.head is None:
            return

         swapped = True
         while swapped:
            swapped = False
            current = self.head

            while current.next is not None:
                if current.name > current.next.name:
                    current.name, current.next.name = current.next.name, current.name
                    current.phone_number, current.next.phone_number = current.next.phone_number, current.phone_number
                    swapped = True
                current = current.next

    def structure(self):
        while True:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("1. Create Contact")
            print("2. Display Contacts")
            print("3. Search Contact")
            print("4. Delete Contact")
            print("5. Edit Contact")
            print("6. Delete All Contacts")
            print("7. Exit")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.create_node()
            elif choice == 2:
                self.display()
            elif choice == 3:
                self.search()
            elif choice == 4:
                self.delete_contact_by_search()
            elif choice == 5:
                self.edit_contacts()
            elif choice == 6:
                self.delete_all_contacts()
            elif choice == 7:
                self.reopen_cb()
                return
            else:
                print("Invalid choice. Please try again.")

    def reopen_cb(self):
        
        temp = self.head
        while temp is not None:
            next_node = temp.next
            del temp
            temp = next_node
        self.head = None

        print("Exiting Contact Book. Goodbye!")

def main():
    cb = ContactBook()
    n = input("What is Your Name: ")
    print("////////\\\\\\\\")
    print(n, "WELCOME TO CONTACTBOOK")
    print("////////\\\\\\\\")
    cb.structure()

if __name__ == "__main__":
    main()