contacts = [
    {"name": "Alice Johnson", "phone": "555-0101", "email": "alice@example.com"},
    {"name": "Ben Smith", "phone": "555-0102", "email": "ben@example.com"},
    {"name": "Chloe Lee", "phone": "555-0103", "email": "chloe@example.com"},
]


def display_contacts(contact_list):
    for contact in contact_list:
        print(f"{contact['name']} | {contact['phone']} | {contact['email']}")


def search_contacts(contact_list, query):
    matches = []
    for contact in contact_list:
        if query.lower() in contact["name"].lower():
            matches.append(contact)
    return matches


# TODO: Add a menu, sorting, create/update/delete contact features, and user interaction.
print("Contact Book")
display_contacts(contacts)
print("\nSearch Example:")
print(search_contacts(contacts, "alice"))
