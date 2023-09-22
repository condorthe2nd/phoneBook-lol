from tkinter import Toplevel, Label, Entry, Button
from manage_contact import manage_contact
from Contact import Contact  # Import the Contact class
from Pickles import save_contacts  # Import the function to save contacts


def create_contact(root, contacts):
    # Create a new window
    new_window = Toplevel(root)
    new_window.title("Add a contact")
    new_window.geometry("300x200")

    # Create a label for the name
    name_label = Label(new_window, text="Name:")
    name_label.grid(row=0, column=0)

    # Create an entry box for the name
    enter_name = Entry(new_window)
    enter_name.grid(row=0, column=1)

    # Create a label for the phone
    phone_label = Label(new_window, text="Phone:")
    phone_label.grid(row=1, column=0)

    # Create an entry box for the phone
    enter_phone = Entry(new_window)
    enter_phone.grid(row=1, column=1)

    # Create a label for the email
    email_label = Label(new_window, text="Email:")
    email_label.grid(row=2, column=0)

    # Create an entry box for the email
    enter_email = Entry(new_window)
    enter_email.grid(row=2, column=1)

    # Create a label for instructions
    label = Label(new_window, text="Fill in the details and click Add")
    label.grid(row=3, columnspan=2)

    def back_button_click():
        new_window.destroy()

    back_button = Button(new_window, text="Back", command=back_button_click)
    back_button.grid(row=4, column=0)

    def add_button_click():
        new_contact = Contact(enter_name.get(), enter_phone.get(), enter_email.get())
        contacts[new_contact.name] = new_contact
        save_contacts(contacts)
        label.config(text=f"Added: {new_contact.name}")

    def on_manage_contact_button_push():
        manage_contact(root, contacts, enter_name.get())
        new_window.destroy()


    add_button = Button(new_window, text="Add", command=add_button_click)
    add_button.grid(row=4, column=1)

    manage_contact_button = Button(new_window, text="Manage Contact", command=on_manage_contact_button_push)
    manage_contact_button.grid(row=4, column=2)
