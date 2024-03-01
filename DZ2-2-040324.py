from collections import UserDict

# Створюємо базовий клас
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

# Клас для зберігання імені контакту в батьківському Field
class Name(Field):
    def __init__(self, value):
        super().__init__(value)

# Клас для зберігання номеру телефону в батьківському Field
class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be 10 digits.")
        super().__init__(value)

# Клас для зберігання інформації з функціональністю
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        if not any(p.value == phone for p in self.phones):
            self.phones.append(Phone(phone))
        else:
            raise ValueError("Phone number already exists for this contact")
        
    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return True
        raise ValueError("Phone number not found for this contact")

    def edit_phone(self, old_phone, new_phone):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        raise ValueError("Phone number not found for this contact")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

# Клас для зберігання та управління записами з функціональністю
class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            raise ValueError("Contact not found")
        

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError("Contact not found")
    

# Приклад використання
if __name__ == "__main__":
    book = AddressBook()

    # Створення запису для John з додаванням до адресної книги
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    if john:
        john.edit_phone("1234567890", "1112223333")

    print(john)

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    if found_phone:
        print(f"{john.name.value}: {found_phone.value}")

    # Видалення запису Jane
    book.delete("Jane")
