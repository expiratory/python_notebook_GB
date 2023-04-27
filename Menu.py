from Notebook import Notebook
from Note import Note
from ImportExport import ImportExport


class Menu:

    notebook = Notebook()
    import_export = ImportExport()

    def __init__(self):
        pass

    def print_menu(self):
        print('Введите цифру, соответствующую желаемому действию: \n'
              '1. Сохранить заметки\n'
              '2. Прочитать заметки\n'
              '3. Добавление заметки\n'
              '4. Редактирование заметки\n'
              '5. Удаление заметки\n')

    def choise_in_menu(self):
        choise = int(input())
        match choise:
            case 1:
                self.import_export.export_note(self.notebook)
            case 2:
                self.import_export.import_note(self.notebook)
            case 3:
                note = Note()
                note.set_title()
                note.set_content()
                self.notebook.add_note(note)
                self.notebook.print_notebook()
            case 4:
                self.notebook.change_note()
            case 5:
                self.notebook.delete_note()

    def start(self):
        self.print_menu()
        self.choise_in_menu()
