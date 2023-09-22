from tkinter import Tk, Button

from Pickles import *
from add_contact_gui import create_contact
from search_gui import find_contact

# now i need to add buttons in each new window to edit the contact found
home_window = Tk()

home_window.title("Contact Manager")

home_window.geometry("400x400")

contacts = load_contacts()


def add_contact():
    create_contact(home_window, contacts)


def lookup_contact():
    find_contact(home_window, contacts)


def exit_app():
    home_window.destroy()


lookup_button = Button(home_window, text="Look up a contact", command=lookup_contact)
add_button = Button(home_window, text="Add a new contact", command=add_contact)

exit_button = Button(home_window, text="Exit", command=exit_app)

# Place buttons on the window
lookup_button.pack()
add_button.pack()
exit_button.pack()

home_window.mainloop()
