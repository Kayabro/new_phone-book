from copy import deepcopy

phone_book = []
old_book = []
path = 'phone_num.txt'


def open_file():
    global phone_book
    global path
    with open(path, 'r', encoding='utf-8') as file:
        data = file.readlines()
        for contact in data:
            new = contact.strip().split(';')
            new_contact = {}
            new_contact['name'] = new[0]
            new_contact['phone'] = new[1]
            new_contact['comment'] = new[2]
            phone_book.append(new_contact)
    old_book = deepcopy(phone_book)
    # print(phone_book)
    # print(old_book)

def get():
    global phone_book
    return phone_book


def add(new_contact: dict):
    global phone_book
    phone_book.append(new_contact)



def save_file():
    global phone_book
    global path
    data = []
    for contact in phone_book:
        data.append(';'.join(contact.values()))
    data = '\n'.join(data)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(data)



def find(find_option: str):
    global phone_book
    all_find = []
    for contact in phone_book:
        for elem in contact.values():
            if find_option in elem:
                all_find.append(contact)
    return all_find




def change_contact(ind: int, contact: dict):
    global phone_book
    phone_book.pop(ind - 1)
    phone_book.insert(ind - 1, contact)


def delete_contact(ind: int):
    global phone_book
    phone_book.pop(ind - 1)


def get_name(ind: int):
    global phone_book
    return phone_book[ind - 1].get('name')


def check_changes():
    global phone_book
    global old_book
    if phone_book != old_book:
        return True
    else:
        return False
