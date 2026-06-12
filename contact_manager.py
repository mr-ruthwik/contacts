class ContactManager:

    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, mobile, mail):

        self.contacts[mobile] = [name, mail]

    def update_contact(self, old_mobile, new_mobile):

        if old_mobile in self.contacts:

            self.contacts[new_mobile] = self.contacts[old_mobile]

            del self.contacts[old_mobile]

            return True

        return False

    def delete_contact(self, mobile):

        if mobile in self.contacts:

            del self.contacts[mobile]

            return True

        return False

    def get_contacts(self):

        return self.contacts