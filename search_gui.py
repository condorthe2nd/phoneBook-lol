from tkinter import Toplevel, Label, Entry, ttk
from style_sheet import get_styles
from Contact import search_contacts
from manage_contact import manage_contact

styles = get_styles()


class FindContact:
    def __init__(self, root, contacts):
        self.result_label = None
        self.entry = None
        self.root = root
        self.contacts = contacts
        self.create_gui()

    def create_gui(self):
        new_window = Toplevel(self.root)
        new_window.config(bg=styles["BG_COLOR"])
        new_window.title("Look up a contact")
        new_window.geometry("300x200")

        style = ttk.Style()
        style.theme_use('alt')

        label = Label(new_window, text="Enter name to search:", bg=styles["BG_COLOR"], font=styles["FONT"])
        label.pack()

        self.entry = Entry(new_window, font=styles["FONT"])
        self.entry.pack()

        search_button = ttk.Button(new_window, text="Search", command=self.search_button_click)
        search_button.pack()

        self.result_label = Label(new_window, text="", bg=styles["BG_COLOR"], font=styles["FONT"])
        self.result_label.pack()

        manage_contact_button = ttk.Button(new_window, text="Manage Contact",
                                           command=lambda: manage_contact(self.root, self.contacts, self.entry.get()))
        manage_contact_button.pack()

        back_button = ttk.Button(new_window, text="Back", command=new_window.destroy)
        back_button.pack()

    def search_button_click(self):
        search_result = search_contacts(self.contacts, self.entry.get())
        if search_result:
            self.result_label.config(text=f"Found: {search_result}")
        else:
            self.result_label.config(text="Contact not found")
