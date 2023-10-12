from tkinter import Tk
from tkinter import Toplevel, Label, Button, messagebox
from tkinter.ttk import Label

from Pickles import *
from manage_contact import manage_contact
from style_sheet import *


# ... Your existing imports and other code
def edit_contact(contact):
    target_contact = contacts.get(contact, None)
    if target_contact is None:
        messagebox.showerror("Error", "Contact not found")
        return
    manage_contact(contacts, target_contact)


def delete_contact(parent, contact):
    parent.destroy()
    if messagebox.askyesno("Confirm", f"Delete {contact}?"):
        if contact in contacts:
            del contacts[contact]
        else:
            messagebox.showerror("Error", "Contact not found")

    # Add logic to delete contact from list here


def on_label_click(contact):
    manage_contact(contacts, contact)


def show_contacts(contacts):
    styles = get_styles()
    contact_list_window = Tk()
    contact_list_window.configure(bg=styles["BG_COLOR"])
    style = ttk.Style()
    style.theme_use('clam')

    contact_list_window.title("Contacts")
    for contact in contacts:
        contact_name = contacts[contact].get_name()
        label = Label(contact_list_window, text=contact_name)
        label.bind("<Button-1>", lambda event, situation=contact: on_label_click(contact_name))
        label.pack()

    def back_button_click():
        contact_list_window.destroy()

    back_button = ttk.Button(contact_list_window, text="Back", command=back_button_click)
    back_button.pack()
