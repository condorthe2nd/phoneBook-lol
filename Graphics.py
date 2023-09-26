from tkinter import Tk, Button
from tkinter import ttk
from Pickles import load_contacts
from add_contact_gui import create_contact
from search_gui import find_contact

# Constants
BG_COLOR = "light grey"
FONT = "Helvetica 14"
ADD_ICON = "\u2795"
SEARCH_ICON = "\U0001F50D"
EXIT_ICON = "\U0001F6AA"

# Root window
home_window = Tk()
home_window.title("Contacts")

# Styling
style = ttk.Style()
style.theme_use('clam')

home_window.config(bg=BG_COLOR)
home_window.option_add("*Font", FONT)

# Functionality
contacts = load_contacts()


def add_contact():
    create_contact(home_window, contacts)


def search_contacts_button():
    find_contact(home_window, contacts)


def exit_app():
    home_window.destroy()


# Buttons
add_contact_button = ttk.Button(home_window, text=f"{ADD_ICON} Add Contact", width=20, command=add_contact)
add_contact_button.grid(pady=20, padx=20)

search_contact_button = ttk.Button(home_window, text=f"{SEARCH_ICON} Search Contacts", width=20,
                                   command=search_contacts_button)
search_contact_button.grid(pady=20, padx=20)

exit_button = ttk.Button(home_window, text=f"{EXIT_ICON} Exit", width=20, command=exit_app)
exit_button.grid(pady=20, padx=20)

home_window.mainloop()
