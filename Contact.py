class Contact:
    def __init__(self, name, phone=None, email=None):
        self.name = name
        self.phone_numbers = [phone] if phone else []
        self.emails = [email] if email else []

    def __str__(self):
        return f"Name: {self.name}, Phone Numbers: {self.phone_numbers}, Emails: {self.emails}"

    def __repr__(self):
        return f"Contact({self.name}, {self.phone_numbers}, {self.emails})"

    def add_email(self, email):
        self.emails.append(email)

    def delete_email(self, email):
        if email in self.emails:
            self.emails.remove(email)

    def add_phone_number(self, phone_number):
        self.phone_numbers.append(phone_number)

    def delete_phone_number(self, phone_number):
        if phone_number in self.phone_numbers:
            self.phone_numbers.remove(phone_number)


def search_contacts(contacts, name):
    for key, value in contacts.items():
        if name in key:
            return value
    return None


def add_email(contact, email):
    contact.emails.append(email)


def delete_email(contact):
    contact.emails = None


def add_phone_number(contact, phone_number):
    contact.phone_numbers.append(phone_number)


def delete_phone_number(contact):
    contact.phone_numbers = None
