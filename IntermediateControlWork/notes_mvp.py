__author__ = 'Alex Bulavin'

from datetime import datetime
import csv
import os
import re


class Note:
    def __init__(self, creation_date, note_id, title_update_date, title,
                 body_update_date, body):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.creation_date = creation_date
        self.title_update_date = title_update_date
        self.body_update_date = body_update_date


class NotesModel:
    def __init__(self):
        self.notes = []

    def load_notes(self, filename):
        # Проверка наличия файла и его создание, если необходимо
        if not os.path.isfile(filename):
            with open(filename, 'w') as file:
                pass

        # Загрузка заметок из CSV файла
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                creation_date, note_id, title_update_date, title, \
                    body_update_date, body = row
                self.notes.append(
                    Note(creation_date, note_id, title_update_date, title,
                         body_update_date, body))

    def save_notes(self, filename):
        # Сохранение заметок в CSV файл
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for note in self.notes:
                writer.writerow([note.creation_date,
                                 note.note_id,
                                 note.title_update_date,
                                 note.title,
                                 note.body_update_date,
                                 note.body])

    def delete_note_by_id(self, note_id, filename):
        for note in self.notes:
            if note.note_id == note_id:
                self.notes.remove(note)
                print(f"Заметка с ID {note_id} успешно удалена.")
                self.save_notes(filename)
                return
        print(f"Заметка с ID {note_id} не найдена.")


class NotesPresenter:
    def __init__(self, model):
        self.model = model

    def print_note_list(self, detailed=False):
        if not self.model.notes:
            print("Пока не создано ни одной заметки.")
            return

        for note in self.model.notes:
            if detailed:
                self.creation_print(note, "")
            else:
                print(f'\033[94mID: \033[92m{note.note_id}\t'
                      f'\033[94mЗаголовок: \033[92m{note.title}\t'
                      f'\033[94mОписание \033[92m{note.body}')

    def add_note(self, filename):
        title = input('Введите заголовок для новой заметки: ')
        body = input('Введите описание заметки: ')
        note_id = len(self.model.notes) + 1
        creation_date = datetime.now().replace(microsecond=0)
        title_update_date = creation_date
        body_update_date = creation_date
        note = Note(creation_date, note_id, title_update_date, title,
                    body_update_date, body)
        self.model.notes.append(note)
        self.creation_print(note, f'\033[94mЗаметка успешно создана!\n')
        self.model.save_notes(filename)
        self.view_menu(filename)

    def creation_print(self, note, action):
        print(
            f'{action}'
            f'\033[94mДата и время сохранения: \033[92m{note.creation_date} \n'
            f'\033[94mID заметки: \033[92m{note.note_id}\n'
            f'\033[94mДата изменения заголовка: '
            f'\033[92m{note.title_update_date}\n'
            f'\033[94mЗаголовок: \033[92m{note.title}\n'
            f'\033[94mДата изменения описания:'
            f'\033[92m{note.body_update_date}\n'
            f'\033[94mОписание:\033[92m{note.body}\n')

    def menu_print(self, has_data):
        if has_data:
            print('\n\033[94mДля просмотра краткого списка всех заметок '
                  'введите ls '
                  '\nДля просмотра полного списка всех заметок введите ll'
                  '\nДля выбора и просмотра/редактирования конкретной заметки '
                  'введите команду select <ID заметки> '
                  '\nДля выбора и просмотра/редактирования диапазона заметок '
                  'за '
                  'период времени введите команду tselect'
                  '\nДля удаления заметки введите команду delete и '
                  'нажмите Enter'
                  '\033[0m')
        print('\033[94mДля добавления новой заметки введите команду add и '
              'нажмите Enter'
              '\nДля выхода из программы введите exit или quit'
              '\033[0m')

    def print_notes_in_range(self, start_date_str, end_date_str,
                             detailed=False):

        if not self.model.notes:
            print("Пока не создано ни одной заметки.")
            return

        filtered_notes = []
        for note in self.model.notes:
            if start_date_str <= \
                    datetime.strptime(note.creation_date,
                                      '%Y-%m-%d %H:%M:%S') <= end_date_str:
                filtered_notes.append(note)

        for note in filtered_notes:
            if detailed:
                self.creation_print(note, "")
            else:
                print(f'\033[94mID: \033[92m{note.note_id}\t'
                      f'\033[94mЗаголовок: \033[92m{note.title}\t'
                      f'\033[94mОписание: \033[92m{note.body}')

    def print_note_list_dialog(self, ):
        choice = input("Выберите формат списка (полный - ll / краткий - ls): ")
        if choice.lower() == 'll':
            return True
        elif choice.lower() == 'ls':
            return False
        else:
            print("Некорректный выбор формата списка.")

    def view_menu(presenter, filename):
        presenter.model.load_notes(filename)
        has_data = len(presenter.model.notes) > 0

        while True:
            presenter.menu_print(has_data)
            command = input("Введите команду: ")

            if command.lower() == 'ls':
                presenter.print_note_list()
            elif command.lower() == 'll':
                presenter.print_note_list(detailed=True)
            elif command.lower().startswith('select'):
                try:
                    note_id = command.split(" ")[1]
                    note = next((note for note in presenter.model.notes
                                 if note.note_id == note_id), None)
                    if note is not None:
                        presenter.creation_print(note, '')
                        new_title = input('Введите новый заголовок заметки: ')
                        if new_title:
                            note.title = new_title
                            note.title_update_date = \
                                datetime.now().replace(microsecond=0)

                        new_body = input('Введите новое описание: ')
                        if new_body:
                            note.body = new_body
                            note.body_update_date = \
                                datetime.now().replace(microsecond=0)

                        presenter.creation_print(note, f'\n\033[94mЗаметка '
                                                       f'успешно '
                                                       f'сохранена!\n\n')
                    else:
                        print(f'Заметка с ID {note_id} не найдена')
                except (ValueError, IndexError):
                    print("Формат команды неверный. Используйте select 1, "
                          "select 2 и так далее")
            elif command.lower() == 'add':
                presenter.add_note(filename)
            elif command.lower() == 'tselect':
                prnt_note_list_dialog = presenter.print_note_list_dialog()

                start_date = input(
                    'Введите начальную дату (Год, Месяц, День): ')
                end_date = input('Введите конечную дату (Год, Месяц, День): ')

                try:
                    start_year, start_month, \
                        start_day = map(int, re.split(r'[,\.]', start_date))
                    end_year, end_month, \
                        end_day = map(int, re.split(r'[,\.]', end_date))

                    start_date = datetime(start_year, start_month, start_day)
                    end_date = datetime(end_year, end_month, end_day)

                    presenter.print_notes_in_range(start_date,
                                                   end_date,
                                                   prnt_note_list_dialog)

                except ValueError:
                    print("Некорректный формат даты. Попробуйте снова.")
            elif command.lower() == 'exit' or command.lower() == 'quit':
                print(
                    '\033[92mБлагодарю за использование этого ПО!\nАвтор: '
                    'Александр Булавин\n22.07.2023\033[0m')
                break
            elif command == "delete":
                note_id = input("Введите ID заметки для удаления: ")
                model.delete_note_by_id(note_id, filename)
            else:
                print('Некорректная команда.')
                presenter.menu_print()

        # presenter.model.save_notes(filename)


if __name__ == "__main__":
    filename = 'notes.csv'
    model = NotesModel()
    presenter = NotesPresenter(model)
    presenter.view_menu(filename)
