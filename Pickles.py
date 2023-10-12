# Pickles.py
import pickle as yummy
from Contact import Contact


def save_contacts(contacts, filename='contacts'):
    with open(filename, 'wb') as f:
        yummy.dump(contacts, f)


def load_contacts(filename='contacts'):
    try:
        with open(filename, 'rb') as f:
            return yummy.load(f)
    except FileNotFoundError:
        return []  # Return an empty list if the file is not found


contacts = load_contacts()
