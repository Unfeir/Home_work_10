from entitys import AddressBook, Record, Name, Phone

my_dict = AddressBook()

def input_error(func):
    """Всі помилки введення користувача повинні оброблятися за допомогою декоратора input_error. 
       Цей декоратор відповідає за повернення користувачеві повідомлень виду:
       "Enter user name", "Give me name and phone please" і т.п. 
       Декоратор input_error обробляє вийнятки
       що виникають у функціях-handler (KeyError, ValueError, IndexError) та повертати відповідну відповідь користувачеві."""
       
    def wraper(*args):
        
        try:
            result = func(*args)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Wrong phone number" 
        except IndexError:
            return "Give me name and phone please"
        except:
            return "Something going wrong" 
        else:
            return result
        
    return wraper


def parser(text):
    if text:
        a = text.replace("good bye", "good_bye").replace("show all", "show_all")
        return a.split()[0], a.split()[1:] # формуємо кортеж із назви функції і аргументів для неї
    
              

@input_error
def hello(*args):
    """ відповідає у консоль "How can I help you?"""
    return "How can I help you?"

@input_error    
def good_bye(*args):
    ''' "good bye", "close", "exit" по будь-якій з цих команд бот завершує свою роботу після того, як виведе у консоль "Good bye!".'''
    return "Good bye!"

    
@input_error
def add_func(args):
    """За цією командою бот зберігає у пам'яті (у словнику наприклад) новий контакт. 
    При наявності контакту з таким іменем дописує телефон/телефони до переліку існуючих, ігнруючи дублі
    Замість ... користувач вводить ім'я та номер телефону, обов'язково через пробіл."""
    name = args[0].capitalize()
    phones = args[1:]
    if name in my_dict.data.keys():
        for phone in phones:
            if int(phone) not in my_dict[name].get_phones():
                my_dict[name].add_phone(int(phone))
        return f"{', '.join(phones)} was added to {name}" 
    else:
        my_dict.add_record(Record(name))
        if phones:
            for phone in phones:
                if int(phone) not in my_dict[name].get_phones():
                    my_dict[name].add_phone(int(phone))
    
        return f"{name} was added with {', '.join(phones)}" 


@input_error
def change_func(args):
    """За цією командою бот зберігає в пам'яті новий номер телефону існуючого контакту. 
    Замість ... користувач вводить ім'я та номер телефону, обов'язково через пробіл."""
    name = args[0].capitalize()
    phone = int(args[1])
    new_phone = int(args[2])
    my_dict[name].change_phone(phone, new_phone)
    return f"{name}`s phone was changed from {phone} to {new_phone}"
    
       
@input_error
def phone_func(args):
    """За цією командою бот виводить у консоль номер телефону для зазначеного контакту. 
    Замість ... користувач вводить ім'я контакту, чий номер треба показати."""
    name = args[0].capitalize()
    all_phones = list(map(lambda x: str(x), my_dict[name].get_phones()))
    return f"{name}`s phone number is {', '.join(all_phones)}"

@input_error
def dell_func(args):
    """За цією командою бот видаляє номер телефону для зазначеного контакту. 
    Замість ... користувач вводить ім'я контакту, чий номер треба показати."""
    name = args[0].capitalize()
    phone = int(args[1])
    if phone in my_dict[name].get_phones():
        my_dict[name].del_phone(phone)
        return f"{name}`s phone number '{phone}' was delleted"
    else:
        return f"{name} have no such number:'{phone}' "

@input_error
def show_all_func(*args):
    """За цією командою бот виводить всі збереженні контакти з номерами телефонів у консоль."""
    contacts = ""
    
    for k, v in my_dict.data.items():
        
        contacts += f"{k} - {my_dict[k].get_phones()}\n"
    
    return contacts
        


def fun_name(fun):
    fun_dict = {
        "hello": hello,
        "good_bye": good_bye,
        "close": good_bye,
        "exit": good_bye,
        "add": add_func,
        "change": change_func,
        "dellete": dell_func,
        "dell": dell_func,
        "phone": phone_func,
        "show_all": show_all_func    
    }
    
    return fun_dict.get(fun)


def main():
       
    go_on = True
    while go_on:
        user_input = input("Listen You: ").lower()
        fun, args = parser(user_input)
        call_fun = fun_name(fun)
        
        if call_fun:
            
            text = call_fun(args)
            print(text)
            if text == "Good bye!":
                go_on = False
            
        
        else:
            print("No such command, try: add, change, show all")
            continue
        
        


main()
