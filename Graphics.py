#edit button still saying contacts not found
# check windwow sizes for all files #
#
from tkinter import Tk
from tkinter import ttk

from show_contacts import show_contacts
from style_sheet import get_styles
from Pickles import *
from add_contact_gui import create_contact
from search_gui import FindContact




# Create a label for the title
styles = get_styles()

ADD_ICON = "\u2795"
SEARCH_ICON = "\U0001F50D"
EXIT_ICON = "\U0001F6AA"

# Root window
home_window = Tk()
home_window.configure(bg=styles["BG_COLOR"])
home_window.title("Contacts")

# Styling
style = ttk.Style()
style.theme_use('clam')
styles['configure_button_style']()

# Functionality


print("Debug: Type of contacts:", type(contacts))
print("Debug: Sample content:", dict(list(contacts.items())[:3]))


def add_contact():
    create_contact(contacts)


def search_contacts_button():
    FindContact(home_window, contacts)


def list_contacts():
    show_contacts(contacts)


def exit_app():
    save_contacts(contacts)
    home_window.destroy()


# Buttons
add_contact_button = ttk.Button(home_window, text=f"{ADD_ICON} Add Contact", width=20, command=add_contact,
                                style="Rounded.TButton")
add_contact_button.grid(pady=20, padx=20)

search_contact_button = ttk.Button(home_window, text=f"{SEARCH_ICON} Search Contacts", width=20,
                                   command=search_contacts_button, style='Rounded.TButton')
search_contact_button.grid(pady=20, padx=20)

list_contacts_button = ttk.Button(home_window, text=f"{SEARCH_ICON} List Contacts", width=20,
                                  command=lambda: list_contacts(), style='Rounded.TButton')
list_contacts_button.grid(pady=20, padx=20)

exit_button = ttk.Button(home_window, text=f"{EXIT_ICON} Exit", width=20, command=exit_app, style='Rounded.TButton')
exit_button.grid(pady=20, padx=20)

home_window.mainloop()
save_contacts(contacts)
