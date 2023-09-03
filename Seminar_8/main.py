def find_desired_contact(phonebook, search_key):
    matches = search_contact(phonebook, search_key)
    desired_contact = None
    if matches:
        if len(matches) > 1:
            print('Найдено более одного совпадения:')
            show_all_contacts(matches)
            while True:
                try:
                    index = int(input('Введите номер искомого контакта: '))
                    if index - 1 in range(len(matches)):
                        desired_contact = matches[index - 1]
                        break
                    else:
                        print('Введен неверный номер контакта. Повторите ввод.')
                except TypeError:
                    print('Введен недопустимый номер контакта.')
        else:
            desired_contact = matches[0]
    return desired_contact
def change_contact (phonebook, search_key):
    changeable_contact = find_desired_contact(phonebook, search_key)
    if changeable_contact:
        print('Изменяемый контакт:')
        show_all_contacts([changeable_contact])
        for contact in phonebook:
            if contact == changeable_contact:
                while True:
                    print('Список доступных команд:')
                    print('1. Изменить фамилию.')
                    print('2. Изменить имя.')
                    print('3. Изменить отчество.')
                    print('4. Изменить номер телефона.')
                    print('5. Закончить изменения.')
                    choice = input('Введите номер команды: ')
                    match choice:
                        case '1':
                            print(f"Текущая фамилия: {contact['last_name']}")
                            contact['last_name'] = input('Введите новую фамилию контакта: ')
                        case '2':
                            print(f"Текущее имя: {contact['first_name']}")
                            contact['first_name'] = input('Введите новое имя контакта: ')
                        case '3':
                            print(f"Текущее отчество: {contact['middle_name']}")
                            contact['middle_name'] = input('Введите новое отчество контакта: ')
                        case '4':
                            print(f"Текущее номер телефона {contact['phone_number']}")
                            contact['phone_number'] = f"{input('Введите новый номер телефона контакта: ')}\n"
                        case '5':
                            break
                        case _:
                            print('Вы ввели неверну команду. Пожалуйста повторите ввод.')
                    print('Измененный контакт: ')
                    show_all_contacts([contact])
    else:
        print('Изменение невозможно, т.к. такого контакта нет в телефонной книге.')
    return phonebook
def delete_one_contact(phonebook, search_key):
    deleting_contact = find_desired_contact(phonebook, search_key)
    if deleting_contact:
        print('Контакт {')
        show_all_contacts([deleting_contact])
        print('} будет удален.')
        choice = input('Вы уверены (Да/Нет): ')
        if choice == 'Да':
            phonebook.remove(deleting_contact)
            print(f'Контакт был успешно удален')
        else:
            print('Повторите выбор команды.')
    else:
        print('Удаление невозможно, т.к. такого контакта нет в телефонной книге.')
    return phonebook
def search_contact(phonebook, search_key):
    results = []
    for contact in phonebook:
        if search_key.lower() in contact['last_name'].lower() or search_key.lower() in contact['first_name'].lower():
            results.append(contact)
    if not results:
        print('Контакт не найден.')
    return results
def load_file(filename):
    phonebook = []
    with open(filename, 'r') as file:
        for contact in file:
            last_name, first_name, middle_name, phone_number = contact.split(' ')
            phonebook.append({'last_name': last_name,
                              'first_name': first_name,
                              'middle_name': middle_name,
                              'phone_number': phone_number})
    return phonebook
def delete_all_contacts(filename, phonebook):
    open(filename, 'w').close()
    return phonebook.clear()
def show_all_contacts(phonebook):
    for index, contact in enumerate(phonebook, start=1):
        print(f"{index}. {contact['last_name']} {contact['first_name']} {contact['middle_name']} {contact['phone_number']}", end =' ')
def save_to_file(filename, phonebook):
    with open(filename, 'w') as file:
        for contact in phonebook:
            file.write(f"{contact['last_name']} {contact['first_name']} {contact['middle_name']} {contact['phone_number']}")
    print ("Данные сохранены.")
def add_contact(phonebook):
    contact = {
        'last_name': input('Введите фамилию: '),
        'first_name': input('Введите имя: '),
        'middle_name': input('Введите отчество: '),
        'phone_number': f"{input('Введите номер: ')}\n"
    }
    phonebook.append(contact)
    print("Контакт добавлен.")
def get_users_command(filename, phonebook):
    while True:
        print('Список команд:')
        print('1. Добавить контакт.')
        print('2. Сохранить файл.')
        print('3. Вывести все контакты.')
        print('4. Поиск по имени/фамилии.')
        print('5. Удалить все контакты.')
        print('6. Удалить отдельный контакт.')
        print('7. Изменить контакт.')
        print('8. Выход.')
        choice = input('Введите номер команды: ')
        match choice:
            case '1':
                add_contact(phonebook)
            case '2':
                save_to_file(filename, phonebook)
            case '3':
                show_all_contacts(phonebook)
            case '4':
                search_key = input('Введите имя или фамилию контакта: ')
                matches = search_contact(phonebook, search_key)
                print('Совпадения: ')
                show_all_contacts(matches)
            case '5':
                print('Вы уверены, что хотите безвозвратно удалить все контакты?')
                choice = input('Да/Нет:')
                if choice == 'Да':
                    phonebook = delete_all_contacts(filename, phonebook)
                else:
                    print('Повторите выбор команды.')
            case '6':
                search_key = input('Введите имя или фамилию контакта, который должен быть удален: ')
                phonebook = delete_one_contact(phonebook, search_key)
                save_to_file(filename, phonebook)
            case '7':
                search_key = input('Введите имя или фамилию контакта, который должен быть изменен: ')
                phonebook = change_contact(phonebook, search_key)
                save_to_file(filename, phonebook)
            case '8':
                break
            case _:
                print('Вы ввели неверну команду. Пожалуйста повторите ввод.')
def main():
    filename = 'contacts.txt'
    phonebook = []
    phonebook = load_file(filename)
    get_users_command(filename, phonebook)

main()

