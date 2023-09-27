from tkinter import Entry, Tk

from Contact import Contact  # Import the Contact class
from Pickles import save_contacts  # Import the function to save contacts
from manage_contact import *
from style_sheet import get_styles

styles = get_styles()


ADD_ICON = "\u2795"  # Add icon


def create_contact(root, contacts):
    # Create a new window
    contact_creation_window = Tk()
    contact_creation_window.configure(bg=styles["BG_COLOR"])
    style = ttk.Style()
    style.theme_use('clam')

    contact_creation_window.title("Add a contact")

    # Create a label for the name
    name_label = Label(contact_creation_window, text="Name:")
    name_label.grid(row=0, column=0)

    # Create an entry box for the name
    enter_name = Entry(contact_creation_window)
    enter_name.grid(row=0, column=1)

    # Create a label for the phone
    phone_label = Label(contact_creation_window, bg=styles["BG_COLOR"], font=styles["FONT"], text="Phone:")
    phone_label.grid(row=1, column=0)

    # Create an entry box for the phone
    enter_phone = Entry(contact_creation_window)
    enter_phone.grid(row=1, column=1)

    # Create a label for the email
    email_label = Label(contact_creation_window, bg=styles["BG_COLOR"], font=styles["FONT"], text="Email:")
    email_label.grid(row=2, column=0)

    # Create an entry box for the email
    enter_email = Entry(contact_creation_window)
    enter_email.grid(row=2, column=1)

    # Create a label for instructions
    label = Label(contact_creation_window, bg=styles["BG_COLOR"], font=styles["FONT"], text="Fill in the details and "
                                                                                            "click Add")
    label.grid(row=3, columnspan=2)

    def back_button_click():
        contact_creation_window.destroy()

    back_button = ttk.Button(contact_creation_window, text="Back", command=back_button_click)
    back_button.grid(row=4, column=0)

    manage_contact_button = ttk.Button(contact_creation_window, text="Manage Contact",
                                       command=lambda: manage_contact(root, contacts, enter_name.get()))
    manage_contact_button.grid(row=4, column=1)

    def add_button_click():
        new_contact = Contact(enter_name.get(), enter_phone.get(), enter_email.get())
        contacts[new_contact.name] = new_contact
        save_contacts(contacts)
        label.config(text=f"Added: {new_contact.name}")

    # Function for add button
    add_button = ttk.Button(contact_creation_window, text="Add", command=add_button_click)
    add_button.grid(row=4, column=2)
