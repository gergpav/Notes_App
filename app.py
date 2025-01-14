import os
import re


def build_note(note_text, note_name):
    """Функция создания текстового файла заметки с обработкой ошибок."""
    try:
        try:
            with open(f'{note_name}.txt', 'r+', encoding='utf-8'):
                print('Такой файл существует')
        except IOError:
            with open(f'{note_name}.txt', 'w+', encoding='utf-8'):
                print('Файл создан')
        with open(f'{note_name}.txt', 'a', encoding='utf-8') as created_file:
            created_file.write(note_text)
            print(f'Заметка {note_name} создана')
    except Exception as e:
        print("Что-то пошло не так. Попробуйте еще раз.", e)

def create_note():
    """
    Функция ввода названия и текста заметки и обработка ошибки при резком выходе из программы.
    При создании названия заметки производится проверка на ввод запретных символов.
    В конце вызывается функция создания текстового файла.
    """
    # Обработка ошибок ввода названия заметки
    while True:
        try:
            note_name = input('Введите название заметки: ')
            forbidden_symbols = "\\|/*<>?:"  # набор запрещенных символов для Windows
            pattern = "[{0}]".format(forbidden_symbols)
            if re.search(pattern, note_name):
                print("Вы ввели недопустимые символы в названии файла. Переименуйте заметку.")
            else:
                print("Название заметки создано.")
                break
        except KeyboardInterrupt:
            print('\nВы вышли из приложения.')
        except Exception as e:
            print("Что-то пошло не так. Попробуйте еще раз.", e)

    # Обработка ошибок ввода текста заметки
    while True:
        try:
            note_text = input('Введите текст заметки: ')
            break
        except KeyboardInterrupt:
            print('\nВы вышли из приложения.')
        except Exception as e:
            print("Что-то пошло не так. Попробуйте еще раз.", e)

    build_note(note_text, note_name)


def read_note():
    """
    Функция чтения заметки.
    Обрабатываются ошибки при вводе существующей заметки, и затем выводится ее текст.
    """
    while True:
        try:
            read_note_name = input('Введите название существующей заметки: ')
            break
        except KeyboardInterrupt:
            print('\nВы вышли из приложения.')
        except Exception as e:
            print("Что-то пошло не так. Попробуйте еще раз.", e)
    note_path = f'{read_note_name}.txt'
    if os.path.isfile(note_path):
        with open(f'{read_note_name}.txt', 'r', encoding='UTF-8') as read_file:
            created_note_text = read_file.read()
            print(f'Текст заметки:\n{created_note_text}')
    else:
        print('Такой заметки не существует.')


def edit_note():
    while True:
        try:
            edit_note_name = input('Введите название существующей заметки: ')
            break
        except KeyboardInterrupt:
            print('\nВы вышли из приложения.')
        except Exception as e:
            print("Что-то пошло не так. Попробуйте еще раз.", e)

    note_path = f'{edit_note_name}.txt'

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
        except Exception as e:
            print("Что-то пошло не так. Попробуйте еще раз.", e)

    note_path = f'{delete_note_name}.txt'

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
        for text in sorted_display_texts:
            print(f'Заметки в порядке от самой короткой до самой длинной: {text}')
    else:
        sorted_display_texts = sorted(display_texts, key=lambda x: len(x), reverse=True)
        for text in sorted_display_texts:
            print(f'Заметки в порядке от самой длинной до самой короткой: {text}')


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


main()