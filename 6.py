from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        self.validate(value)
        super().__init__(value)

    @staticmethod
    def validate(value):
        if not re.fullmatch(r'\d{10}', value):
            raise ValueError("Phone number must contain exactly 10 digits")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        phone_obj = Phone(phone)
        self.phones = [p for p in self.phones if p.value != phone_obj.value]

    def edit_phone(self, old_phone, new_phone):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone):
        phone_obj = Phone(phone)
        return phone_obj in self.phones

    def __str__(self):
        phones_str = '; '.join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find_record(self, name):
        return self.data.get(name)

    def delete_record(self, name):
        if name in self.data:
            del self.data[name]

    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())

# Приклад використання
if __name__ == "__main__":
    address_book = AddressBook()

    record1 = Record("Alice")
    record1.add_phone("1234567890")
    record1.add_phone("0987654321")

    record2 = Record("Bob")
    record2.add_phone("1122334455")

    address_book.add_record(record1)
    address_book.add_record(record2)

    print("Address book:")
    print(address_book)

    print("\nFinding record for Alice:")
    print(address_book.find_record("Alice"))

    print("\nDeleting record for Bob")
    address_book.delete_record("Bob")
    print(address_book)
