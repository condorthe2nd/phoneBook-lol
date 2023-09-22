def search_contacts(contacts, name):
    for key, value in contacts.items():
        if name in key:
            return str(contacts[key])
    return None
