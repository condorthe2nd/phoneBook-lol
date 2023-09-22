class Contact:
    def __init__(self, name, phone=None, email=None):
        self.name = name
        self.phone_numbers = [phone] if phone else []
        self.emails = [email] if email else []

    def __str__(self):
        return f"Name: {self.name}, Phone Numbers: {self.phone_numbers}, Emails: {self.emails}"

    def __repr__(self):
        return f"Contact({self.name}, {self.phone_numbers}, {self.emails})"
