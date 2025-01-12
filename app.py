import os


def build_note(note_text, note_name):
    with open(f'{note_name}.txt', 'w', encoding='utf-8') as new_file:
        new_file.write(note_text)
    print(f'Заметка {note_name} создана')

def create_note():
    note_name = input('Введите название заметки: ')
    note_text = input('Введите текст заметки: ')
    build_note(note_name, note_text)


def read_note():
    read_note_name = input('Введите название существующей заметки: ')
    note_path = f'C:\\Users\\ПавловГеоргийСергеев\\PycharmProjects\\Notes_App\\{read_note_name}.txt'
    if os.path.isfile(note_path):
        with open(f'{read_note_name}.txt', 'r', encoding='UTF-8') as read_file:
            created_note_text = read_file.read()
            print(created_note_text)
    else:
        print('Такой заметки не существует.')


def edit_note():
    edit_note_name = input('Введите название существующей заметки: ')
    note_path = f'C:\\Users\\ПавловГеоргийСергеев\\PycharmProjects\\Notes_App\\{edit_note_name}.txt'
    if os.path.isfile(note_path):
        with open(f'{edit_note_name}.txt', 'w', encoding='UTF-8') as edit_file:
            new_note_text = input('Введите новый текст заметки: ')
            edited_note_text = edit_file.write(new_note_text)
            print(edited_note_text)
    else:
        print('Такой заметки не существует.')

def delete_note():
    delete_note_name = input('Введите название существующей заметки: ')
    note_path = f'C:\\Users\\ПавловГеоргийСергеев\\PycharmProjects\\Notes_App\\{delete_note_name}.txt'
    if os.path.isfile(note_path):
        os.remove(note_path)

def display_notes():
    notes = [note for note in os.listdir() if note.endswith(".txt")]
    print(notes)

def main():
    print("""
Меню: 
1. Создать заметку
2. Прочитать заметку
3. Редактировать заметку
4. Удалить заметку
5. Посмотреть все заметки
6. Выход
    """)

    choice = input('Выберите действие: ')

    if choice == '1':
        create_note()
    if choice == '2':
        read_note()
    if choice == '3':
        edit_note()
    if choice == '4':
        delete_note()
    if choice == '5':
        display_notes()


if __name__ == '__main__':
    main()