from tkinter import Tk
from tkinter.ttk import Label

from style_sheet import *


def on_label_click(event, contact):
    pass


def show_contacts(contacts):
    styles = get_styles()
    contact_list_window = Tk()
    contact_list_window.configure(bg=styles["BG_COLOR"])
    style = ttk.Style()
    style.theme_use('clam')

    contact_list_window.title("Contacts")
    counter = 0
    for contact in contacts:
        contact_name = contact.get_name()
        label = Label(contact_list_window, text=contact_name)
        label.bind(f"<Button-{counter}>", lambda event, situation=contact: on_label_click(event, situation))
        label.pack()

    def back_button_click():
        contact_list_window.destroy()

    back_button = ttk.Button(contact_list_window, text="Back", command=back_button_click)
    back_button.pack()
