__author__ = 'Alex Bulavin'

import csv
from datetime import datetime
import os


class Note:
    def __init__(self, creation_date, note_id, title_update_date, title,
                 body_update_date, body):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.creation_date = creation_date
        self.title_update_date = title_update_date
        self.body_update_date = body_update_date


class NotesManager:
    def __init__(self):
        self.notes = []

    def load_notes(self):
        # Проверка наличия файла и его создание, если необходимо
        if not os.path.isfile('notes.csv'):
            with open('notes.csv', 'w') as file:
                pass

        # Загрузка заметок из CSV файла
        with open('notes.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                creation_date, note_id, title_update_date, title, body_update_date, body = row
                self.notes.append(
                    Note(creation_date, note_id, title_update_date, title,
                         body_update_date, body))

    def save_notes(self):
        # Сохранение заметок в CSV файл
        with open('notes.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for note in self.notes:
                writer.writerow([note.creation_date,
                                 note.note_id,
                                 note.title_update_date,
                                 note.title,
                                 note.body_update_date,
                                 note.body])

    def print_note_list(self, detailed=False):

        for note in self.notes:

            if detailed:
                self.creation_print(note, "")

            else:
                print(f'\033[94mID: \033[92m{note.note_id}\t'
                      f'\033[94mЗаголовок: \033[92m{note.title}\t'
                      f'\033[94mОписание \033[92m{note.body}')

    def add_note(self):
        title = input('Введите заголовок для новой заметки: ')
        body = input('Введите описание заметки: ')
        note_id = len(self.notes) + 1
        creation_date = datetime.now().replace(microsecond=0)
        title_update_date = creation_date
        body_update_date = creation_date
        note = Note(creation_date, note_id, title_update_date, title,
                    body_update_date, body)
        self.notes.append(note)
        self.creation_print(note, f'\033[94mЗаметка успешно создана!\n')
        manager.save_notes()
        menu_print()

    def creation_print(self, note, action):
        print(
            f'{action}'
            f'\033[94mДата и время сохранения: \033[92m{note.creation_date} \n'
            f'\033[94mID заметки: \033[92m{note.note_id}\n'
            f'\033[94mДата изменения заголовка: \033[92m{note.title_update_date}\n '
            f'\033[94mЗаголовок: \033[92m{note.title}\n'
            f'\033[94mДата изменения описания:\033[92m{note.body_update_date}\n'
            f'\033[94mОписание:\033[92m{note.body}\n')

    def select_note(self, note_id):
        # note = next((note for note in self.notes if note.note_id == note_id),
        #             None)
        note = next(
            (note for note in manager.notes if note.note_id == note_id), None)

        if note:
            self.creation_print(note, '')
            new_title = input('Введите новый заголовок заметки: ')
            if new_title:
                note.title = new_title
                note.title_update_date = datetime.now().replace(microsecond=0)

            new_body = input('Введите новое описание: ')
            if new_body:
                note.body = new_body
                note.body_update_date = datetime.now().replace(microsecond=0)

            self.creation_print(note, f'\n\033[94mЗаметка успешно сохранена!\n\n')

        else:
            print(f'Заметка с ID {note_id} не найдена')

    def delete_note_by_id(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                self.notes.remove(note)
                print(f"Заметка с ID {note_id} успешно удалена.")
                return
        print(f"Заметка с ID {note_id} не найдена.")


def menu_print():
    print('\033[94mДля просмотра краткого списка всех заметок введите ls'
          '\nДля просмотра полного списка всех заметок введите ll'
          '\nДля выбора и просмотра/редактирования конкретной заметки '
          'введите команду select <ID заметки> '
          '\nДля добавления новой заметки введите команду add и '
          'нажмите Enter'
          '\nДля удаления заметки введите команду delete и '
          'нажмите Enter'
          '\nДля выхода из программы введите exit или quit\033[0m')


if __name__ == "__main__":
    manager = NotesManager()
    manager.load_notes()
    print('\033[94mПрограмма для работы с заметками\n')
    while True:
        if manager.notes:
            menu_print()

        else:
            print("Пока нет ни одной заметки.")
            manager.add_note()

        command = input('\033[37m> \033[0m').strip()

        if command.lower() == 'ls':
            manager.print_note_list()
        elif command.lower() == 'll':
            manager.print_note_list(detailed=True)
        elif command.lower().startswith('select'):
            try:
                note_id = command.split()[1]
                manager.select_note(note_id)
            except IndexError:
                print(
                    "Формат команды неверный. Используйте select <ID заметки>")
        elif command.lower() == 'add':
            manager.add_note()
        elif command == "delete":
            note_id = input("Введите ID заметки для удаления: ")
            manager.delete_note_by_id(note_id)
        elif command.lower() == 'exit' or command.lower() == 'quit':
            manager.save_notes()
            print(
                '\033[92mБлагодарю за использование этого ПО!\nАвтор: '
                'Александр Булавин.\033[0m')
            break
