"""
============================
Simple CLI To-Do List App
============================
"""

class ToDoApp:
    def __init__(self):
        self.to_do_list = []

    def display_menu(self):
        print("\nTo-Do List App Menu:")
        print("1. Add To-Do Item")
        print("2. View To-Do List")
        print("3. Delete To-Do Item")
        print("4. Quit")

    def add_item(self):
        item = input("Enter your to-do item: ")
        self.to_do_list.append(item)
        print(f"Added: {item}")

    def view_list(self):
        if not self.to_do_list:
            print("Your to-do list is empty.")
        else:
            print("\nYour To-Do List:")
            for index, item in enumerate(self.to_do_list, start=1):
                print(f"{index}. {item}")

    def delete_item(self):
        if not self.to_do_list:
            print("Your to-do list is empty.")
        else:
            self.view_list()
            try:
                choice = int(input("Enter the number of the item to delete: "))
                if choice < 1 or choice > len(self.to_do_list):
                    print("Invalid choice. Please try again.")
                else:
                    deleted_item = self.to_do_list.pop(choice - 1)
                    print(f"Deleted: {deleted_item}")
            except ValueError:
                print("Invalid input. Please enter a number.")

def main():
    app = ToDoApp()
    while True:
        app.display_menu()
        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                app.add_item()
            elif choice == 2:
                app.view_list()
            elif choice == 3:
                app.delete_item()
            elif choice == 4:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
