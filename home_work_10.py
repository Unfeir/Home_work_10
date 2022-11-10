class UserDict():
    pass

class AddressBook(UserDict): # та ми потім додамо логіку пошуку за записами до цього класу
    
    def __init__(self):
        self.data = {}
        
    def add_record(self, record):
        self.data[record.name.value] = record.phone
        

class Record():  # який відповідає за логіку додавання/видалення/редагування необов'язкових полів та зберігання обов'язкового поля Name.
    
    def __init__(self, name):
        self.name = name
        self.phone = []
    
    def add_phone(self, phone):
        self.phone.append(phone)
        
    def del_phone(self, phone):
        self.phone.remove(phone)
        
    def change_phone(self, phone, new_value):
        
        for item in self.phone:
            if item == phone:
                phone.value = new_value



class Field():  # який буде батьківським для всіх полів, у ньому потім реалізуємо логіку загальну для всіх полів.
    pass
        
       
class Name(Field):  #обов'язкове поле з ім'ям.
    def __init__(self, name):
        super().__init__()
        self.value = name


class Phone(Field): # необов'язкове поле з телефоном та таких один запис (Record) може містити кілька.
    def __init__(self, phone):
        super().__init__()
        self.value = phone

# a = Name("ssss")

# b = Phone(555555)
# b1 = Phone(44444444)
# b2 = Phone(111111)
# c = Record(a)

# c.add_phone(b)
# c.add_phone(b1)
# c.add_phone(b2)

# print(c.name.value)
# print(c.phone)

# c.del_phone(b2)
# print(c.phone)
# c.change_phone(b1, 9999999)
# print(b1.value)

# ad = AddressBook()
# ad.add_record(c)
# ad.add_record(c)
# print(ad.data)