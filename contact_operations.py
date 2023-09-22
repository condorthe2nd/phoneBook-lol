def search_contacts(contacts, name):
    for key, value in contacts.items():
        if name in key:
            return str(contacts[key])
    return None


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