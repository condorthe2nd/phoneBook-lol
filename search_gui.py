from tkinter import Toplevel, Label, Entry, Button

from contact_operations import search_contacts


def find_contact(root, contacts):
    # Create a new window
    new_window = Toplevel(root)
    new_window.title("Look up a contact")
    new_window.geometry("300x200")

    # Add a label and text box for entering the name
    label = Label(new_window, text="Enter name to search:")
    label.pack()

    entry = Entry(new_window)
    entry.pack()

    def back_button_click():
        new_window.destroy()

    # Function for search button
    def search_button_click():
        search_result = search_contacts(contacts, entry.get())
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
