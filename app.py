import os


def build_note(note_text, note_name):
    with open(f'{note_name}.txt', 'w', encoding='utf-8') as new_file:
        new_file.write(note_text)
    print(f'Заметка {note_name} создана')

def create_note():
    while True:
        try:
            note_name = input('Введите название заметки: ')
            break
        except KeyboardInterrupt:
            print('\nВы вышли из приложения.')

    while True:
        try:
            note_text = input('Введите текст заметки: ')
            break
        except KeyboardInterrupt:
            print('\nВы вышли из приложения.')

    build_note(note_text, note_name)


def read_note():
    while True:
        try:
            read_note_name = input('Введите название существующей заметки: ')
            break
        except KeyboardInterrupt:
            print('\nВы вышли из приложения.')
    note_path = f'C:\\Users\\ПавловГеоргийСергеев\\PycharmProjects\\Notes_App\\{read_note_name}.txt'
    if os.path.isfile(note_path):
        with open(f'{read_note_name}.txt', 'r', encoding='UTF-8') as read_file:
            created_note_text = read_file.read()
            print(created_note_text)
    else:
        print('Такой заметки не существует.')


def edit_note():
    while True:
        try:
            edit_note_name = input('Введите название существующей заметки: ')
            break
        except KeyboardInterrupt:
            print('\nВы вышли из приложения.')

    note_path = f'C:\\Users\\ПавловГеоргийСергеев\\PycharmProjects\\Notes_App\\{edit_note_name}.txt'

    if os.path.isfile(note_path):
        with open(f'{edit_note_name}.txt', 'w', encoding='UTF-8') as edit_file:
            new_note_text = input('Введите новый текст заметки: ')
            edited_note_text = edit_file.write(new_note_text)
            print(edited_note_text)
    else:
        print('Такой заметки не существует.')

def delete_note():
    while True:
        try:
            delete_note_name = input('Введите название существующей заметки: ')
            break
        except KeyboardInterrupt:
            print('\nВы вышли из приложения.')

    note_path = f'C:\\Users\\ПавловГеоргийСергеев\\PycharmProjects\\Notes_App\\{delete_note_name}.txt'

    if os.path.isfile(note_path):
        os.remove(note_path)
    else:
        print('Такой заметки не существует.')

def display_notes():
    notes = [note for note in os.listdir() if note.endswith(".txt")]
    display_texts = []

    for note in notes:
        with open(note, 'r', encoding='utf-8') as display_file:
            display_text = display_file.read()
            display_texts.append(display_text)

    while True:
        try:
            choice_sort = input('В каком порядке вам вывести заметки по их длине (по возрастанию/по убыванию)? ')
            if choice_sort.lower() != 'по возрастанию' and choice_sort.lower() != 'по убыванию':
                raise ValueError
            else:
                break
        except ValueError:
            print('Вы неверно ввели действие, пожалуйста, выберите одну из двух опций (по возрастанию/по убыванию).')
        except KeyboardInterrupt:
            print('\nВы вышли из приложения.')

    if choice_sort.lower() == 'по возрастанию':
        sorted_display_texts = sorted(display_texts, key=lambda x: len(x))
    else:
        sorted_display_texts = sorted(display_texts, key=lambda x: len(x), reverse=True)
    print(sorted_display_texts)


def main():
    while True:
        while True:
            print("""
Меню: 
1. Создать заметку
2. Прочитать заметку
3. Редактировать заметку
4. Удалить заметку
5. Посмотреть все заметки
6. Выход
                        """)
            try:
                choice = int(input('Выберите действие: '))
                if not isinstance(choice, int) or not 1 <= choice <= 6:
                    raise ValueError
                else:
                    break
            except ValueError:
                print('Вы неверно выбрали опцию, попробуйте снова.')
            except KeyboardInterrupt:
                print('\nВы вышли из приложения.')

        if choice == 1:
            create_note()
        if choice == 2:
            read_note()
        if choice == 3:
            edit_note()
        if choice == 4:
            delete_note()
        if choice == 5:
            display_notes()
        if choice == 6:
            print('\nВы вышли из приложения.')
            break


if __name__ == '__main__':
    main()