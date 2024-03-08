#1. Показывать все контакты
#2. Добавлять контакт
#3. Найти контакт
#4. Изменять контакт
#5.Удалять контакт

#1. Показывать все контакты
def show_all_phones():
    my_data = []
    with open('numbers.txt', 'r', encoding='utf-8') as contact:
        for i in contact:
            my_list = i.split()
            my_data.append(my_list)
            print(*my_list)
    return my_data

#2. Добавлять контакт
def add_new_contact():
    num = int(input("Введите кол-во контактов которые хотите добавить: "))
    with open('numbers.txt', 'a', encoding= 'utf-8') as contact:
        for i in range(num):
            print("Введите данные", i+1 , "контакта: ")
            name = input("Введите имя контакта: ")
            numbers = input("Введите номер контакта: ")
            comment = input("Введите комментарий к номеру контакта: ")
            new_data = f'{name} {numbers} {comment} \n'
            contact.write(new_data)

#3. Найти контакт
def find_all_criteries(text):
    searching_text = text.lower()
    searching_contacts= []
    with open('numbers.txt', 'r', encoding='utf-8') as contact:
        for i in contact:
            my_list = i.lower().split()
            if searching_text in my_list:
                searching_contacts.append(my_list)
    for i in range(len(searching_contacts)):
        print(f'Контакт номером - {i+1}: {searching_contacts[i]}')
    return searching_contacts

#4. Изменять контакт
def change_contact():
    my_data = []
    with open('numbers.txt', 'r', encoding='utf-8') as contact:
        for i in contact:
            my_list = i.lower().split()
            my_data.append(my_list)
    searching_text = input("Найдите контакт который хотите изменить: ").lower()
    my_list = find_all_criteries(searching_text)
    if not my_list:
        return
    num = 0
    if len(my_list)>1:
        num = int(input("Введите номер контакта который хотите изменить: "))
    criterie = int(input("Введите столбец который хотите изменить. 1. Имя 2. Номер 3. Комментарий: "))
    replace = input("Введите текст изменения: ")
    for i in my_data:
        if i == my_list[num-1]:
            for j in range(len(i)):
                if j == criterie-1:
                    i[j] = replace
    with open('numbers.txt', 'w', encoding='utf-8') as contact:
        for i in my_data:
            contact.writelines(f'{i[0]} {i[1]} {i[2]} \n')

#5.Удалять контакт
def remove_contact():
    my_data = []
    with open('numbers.txt', 'r', encoding='utf-8') as contact:
        for i in contact:
            my_list = i.lower().split()
            my_data.append(my_list)
    searching_text = input("Найдите контакт который хотите удалить: ").lower()
    my_list = find_all_criteries(searching_text)
    if not my_list:
        return
    num = 0
    if len(my_list)>1:
        num = int(input("Введите номер контакта который хотите удалить: "))
    for i in my_data:
        if i == my_list[num-1]:
            my_data.remove(i)
    with open('numbers.txt', 'w', encoding='utf-8') as contact:
        for i in my_data:
            contact.writelines(f'{i[0]} {i[1]} {i[2]} \n')

#6.Копировать в другой файл
def copy_file():
    my_data = show_all_phones()
    num_stroka = int(input("Введите номер строки которую хотите скопировать: "))
    if num_stroka<len(my_data):
        new_list = my_data[num_stroka]
        with open('new_files.txt', 'a', encoding='utf-8') as contact:
            contact.write('\n')
            for i in new_list:
                contact.writelines(f'{i} ')


#Сама программа
while True:
    print("""Выберите нужный пункт меню:
    1. Показывать все контакты
    2. Добавлять контакт
    3. Найти контакт
    4. Изменять контакт
    5. Удалять контакт
    6. Копировать в другой файл
    7. Выйти из программы""")
    variable = int(input("Введите нужный пункт меню: "))
    if variable == 3:
        text = input("Введите контакт который ищете: ")
        find_all_criteries(text)
    match variable:
        case 1: show_all_phones()
        case 2: add_new_contact()
        case 4: change_contact()
        case 5: remove_contact()
        case 6: copy_file()
        case 7: break
    if variable>7:
        print("Введите корректную цифру")