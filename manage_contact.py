from Pickles import load_contacts
from style_sheet import get_styles
from tkinter import Toplevel, Label, messagebox, Frame
from tkinter import ttk  # for better styling

styles = get_styles()


def manage_contact(contacts, name):
    # Validate if 'name' exists in 'contacts'
    contact = contacts.get(name, None)
    if contact is None:
        messagebox.showerror("Error", "Contact not found")
        return


    new_window = Toplevel()
    new_window.config(bg=styles["BG_COLOR"])
    new_window.title(f"Managing Contact: {name}")

    style = ttk.Style()
    style.theme_use('clam')
    new_window.option_add("*Font", styles["FONT"])

    # Create a frame for better organization
    frame = Frame(new_window, padx=20, pady=20, bg=styles["BG_COLOR"])
    frame.pack(padx=10, pady=10)

    Label(frame, text=f"Managing Contact: {name}", font=(styles["FONT"], 16), bg=styles["BG_COLOR"]).grid(row=0,
                                                                                                          columnspan=2)

    # Add Email Section
    email_entry = ttk.Entry(frame)
    ttk.Label(frame, text="Add Email:", background=styles["BG_COLOR"]).grid(row=1, column=0)
    email_entry.grid(row=1, column=1)

    def add_email_action():
        email = email_entry.get()
        contact.add_email(email)
        messagebox.showinfo("Success", "Email added successfully")

    ttk.Button(frame, text="Add", command=add_email_action).grid(row=1, column=2)

    # Delete Email Section
    delete_email_entry = ttk.Entry(frame)
    ttk.Label(frame, text="Delete Email:", background=styles["BG_COLOR"]).grid(row=2, column=0)
    delete_email_entry.grid(row=2, column=1)

    def delete_email_action():
        email = delete_email_entry.get()
        if email is None:
            contact.delete_all_email()
        elif email in contact.emails:
            contact.delete_email(email)
            messagebox.showinfo("Success", "Email deleted successfully")
        else:
            messagebox.showerror("Error", "Email not found")

    ttk.Button(frame, text="Delete", command=delete_email_action).grid(row=2, column=2)

    # Add Phone Number Section
    phone_entry = ttk.Entry(frame)
    ttk.Label(frame, text="Add Phone Number:", background=styles["BG_COLOR"]).grid(row=3, column=0)
    phone_entry.grid(row=3, column=1)

    def add_phone_action():
        phone = phone_entry.get()
        contact.add_phone_number(phone)
        messagebox.showinfo("Success", "Phone number added successfully")

    ttk.Button(frame, text="Add", command=add_phone_action).grid(row=3, column=2)

    # Delete Phone Number Section
    delete_phone_entry = ttk.Entry(frame)
    ttk.Label(frame, text="Delete Phone Number:", background=styles["BG_COLOR"]).grid(row=4, column=0)
    delete_phone_entry.grid(row=4, column=1)

    def delete_phone_action():
        phone = delete_phone_entry.get()
        if phone in contact.phone_numbers:
            contact.delete_phone_number(phone)
            messagebox.showinfo("Success", "Phone number deleted successfully")
        else:
            messagebox.showerror("Error", "Phone number not found")

    ttk.Button(frame, text="Delete", command=delete_phone_action).grid(row=4, column=2)

    # Back Button to close the current window and go back to the previous window
    ttk.Button(frame, text="Back", command=new_window.destroy).grid(row=5, columnspan=2)
