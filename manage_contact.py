from tkinter import Toplevel, Label, Entry, Button, messagebox

from Contact import search_contacts, add_email, delete_email, add_phone_number, delete_phone_number


def manage_contact(root, contacts, name):
    # Validate if 'name' exists in 'contacts'
    if not search_contacts(contacts, name):
        messagebox.showerror("Error", "Contact not found")
        return

    # Create a new window
    new_window = Toplevel(root)
    new_window.title("EDIT CONTACT")
    new_window.geometry("400x300")

    def back_button_click():
        new_window.destroy()

    # Add a Back button
    Button(new_window, text="Back", command=back_button_click).grid(row=0, column=0)

    # Email entry box
    Label(new_window, text="Email:").grid(row=1, column=0)
    email_entry = Entry(new_window)
    email_entry.grid(row=1, column=1)
    Button(new_window, text="Add Email",
           command=lambda: add_email(search_contacts(contacts, name), email_entry.get())).grid(row=1, column=2)
    Button(new_window, text="Delete Email",
           command=lambda: delete_email(search_contacts(contacts, name)).grid(row=1, column=3))

    # Phone number entry box
    Label(new_window, text="Phone Number:").grid(row=2, column=0)
    phone_entry = Entry(new_window)
    phone_entry.grid(row=2, column=1)
    Button(new_window, text="Add Phone",
           command=lambda: add_phone_number(search_contacts(contacts, name), phone_entry.get())).grid(row=2, column=2)
    Button(new_window, text="Delete Phone",
           command=lambda: delete_phone_number(search_contacts(contacts, name)).grid(row=2, column=3))
