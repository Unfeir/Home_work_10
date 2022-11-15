from collections import UserDict

class AddressBook(UserDict): # та ми потім додамо логіку пошуку за записами до цього класу
    
    def add_record(self, record):
        self.data[record.name.value] = record
        

class Record:  # який відповідає за логіку додавання/видалення/редагування необов'язкових полів та зберігання обов'язкового поля Name.
    
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
        
    def del_phone(self, phone): # видаляти треба не за екземпляром а за номером з екземпляра            
         for item in self.phones:
            if item.value == phone:
                self.phones.remove(item)
        
    def change_phone(self, phone, new_value):
        for item in self.phones:
            if item.value == phone:
                item.value = new_value
    
    def get_phones(self):
        all_phones = [phone.value for phone in self.phones]
        return all_phones
 

class Field:  # який буде батьківським для всіх полів, у ньому потім реалізуємо логіку загальну для всіх полів.
    def __init__(self, value):
        self.value = value
        
       
class Name(Field):  #обов'язкове поле з ім'ям.
    pass


class Phone(Field): # необов'язкове поле з телефоном та таких один запис (Record) може містити кілька.
    pass
