from tkinter import Toplevel, Label, Button

from contact_operations import search_contacts, add_email, delete_email, add_phone_number, delete_phone_number


def manage_contact(root, contacts,name):
    # Create a new window
    new_window = Toplevel(root)
    new_window.title("Look up a contact")
    new_window.geometry("300x200")

    def back_button_click():
        new_window.destroy()

        Label(new_window, text="add_email").pack()
    Button(new_window, text="add_email", command=lambda: add_email(contacts, name)).pack()

    Label(new_window, text="delete_email").pack()
    Button(new_window, text="delete_email", command=lambda: delete_email(contacts, name)).pack()

    Label(new_window, text="add_phone_number").pack()
    Button(new_window, text="add_phone_number", command=lambda: add_phone_number(contacts, name)).pack()

    Label(new_window, text="delete_phone_number").pack()
    Button(new_window, text="delete_phone_number", command=lambda: delete_phone_number(contacts, name)).pack()

# Function for search button
    def search_button_click():
        search_result = search_contacts(contacts, name)
        if search_result:
            result_label.config(text=f"Found: {search_result}")
        else:
            result_label.config(text="Contact not found")
    # Add a search button
    search_button = Button(new_window, text="Search", command=search_button_click)
    search_button.pack()

    # Label to display search result
    result_label = Label(new_window, text="")
    result_label.pack()

    back_button = Button(new_window, text="Back", command=back_button_click)
    back_button.pack()



