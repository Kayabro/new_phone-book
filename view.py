import view


def menu():
    while True:
        print('''1. Открыть файл
2.Сохранить файл.
3.Показать контакты.
4.Создать контакт.
5.Изменить контакт.
6.Найти контакт.
7.Удалить контакт.
8.Выход''')
        print('Используя цифру от 1 до 8, выберите действие!')
        print('')
        act = input('Какое действие выполнить: ')
        if act.isdigit() == True:
            if 1 <= int(act) <= 8:
                return int(act)
            else:
                print('Цифра должна быть от 1 до 8!')
        else:
            print('Выбрать можно только цифрой от 1 до 8!')


def show_contact(pb: list[dict]):
    if pb == []:
        print('Телефонная книга пуста или файл не открыт')
    else:
        for i, contact in enumerate(pb, 1):
            name = contact.get('name')
            phone = contact.get('phone')
            comment = contact.get('comment')
            print(f'{i}. {name: <20} {phone: <15} {comment: <20} ')


def init_flag():
    print('Файл успешно открыт!')


def new_contact_input():
    name = input('Введите имя и фамилию: ')
    phone = input('Введите номер телефон: ')
    commet = input('Введите комментарий: ')
    new_contact = {}
    new_contact['name'] = name
    new_contact['phone'] = phone
    new_contact['comment'] = commet
    return new_contact


def search_contact():
    search = input('Что ищем: ')
    return search

def input_id():
    index = int(input('Индекс: '))


def confirm(condition: str, name: str):
    answer = input(f'Вы действительно хотите {condition} контакт {name}? (y/n)')
    if answer == 'y':
        return True
    else:
        return False


def confirm_changes():
    anwswer = input('У вас несохраненные изменения, хотите сохранить? (y/n)')
    return True if anwswer == 'y' else False
