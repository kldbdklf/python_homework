def delete_one_contact(phonebook, search_key):
    matches = search_contact(phonebook, search_key)
    removable_contact = None
    if len(matches) > 1:
        print('Найдено более одного совпадения:')
        show_all_contacts(matches)
        while True:
            try:
                index = int(input('Введите номер контакта, который должен быть удален: '))
                if index - 1 in range(len(matches)):
                    removable_contact = matches[index - 1]
                    break
                else:
                    print('Введен неверный номер контакта. Повторите ввод.')
            except TypeError:
                print('Введен недопустимый номер контакта.')
    else:
        removable_contact = matches[0]
    phonebook.remove(removable_contact)
    print(f'Контакт был успешно удален')
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
    print(f'\n_____________________________________________ \n')
    for index, contact in enumerate(phonebook, start=1):
        print(f"{index}. {contact['last_name']} {contact['first_name']} {contact['middle_name']} {contact['phone_number']}", end =' ')
    print(f'\n_____________________________________________ \n')
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
def main():
    filename = 'contacts.txt'
    phonebook = []
    phonebook = load_file(filename)
    while True:
        print('Список команд:')
        print('1. Добавить контакт.')
        print('2. Сохранить файл.')
        print('3. Вывести все контакты.')
        print('4. Поиск по имени/фамилии.')
        print('5. Удалить все контакты.')
        print('6. Удалить отдельный контакт.')
        print('7. Загрузить файл.')
        print('8. Выход.')
        choice = input('Введите номер команды: ')
        if choice == '1':
            add_contact(phonebook)
        elif choice == '2':
            save_to_file(filename, phonebook)
        elif choice == '3':
            show_all_contacts(phonebook)
        elif choice == '4':
            search_key = input('Введите имя или фамилию контакта: ')
            matches = search_contact(phonebook, search_key)
            print('Совпадения: ')
            show_all_contacts(matches)
        elif choice == '5':
            print('Вы уверены, что хотите безвозвратно удалить все контакты?')
            choice = input('Да/Нет:')
            if choice == 'Да':
                phonebook = delete_all_contacts(filename, phonebook)
            else:
                print('Повторите выбор команды.')
        elif choice == '6':
            search_key = input('Введите имя или фамилию контакта, который должен быть удален: ')
            phonebook = delete_one_contact(phonebook, search_key)
            save_to_file(filename, phonebook)
        # elif choice == '7':

        elif choice == '8':
            break
        else:
            print('Вы ввели неверну команду. Пожалуйста повторите ввод.')
main()

