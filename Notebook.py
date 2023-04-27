from Note import Note


class Notebook:

    notebook = []

    def add_note(self, NoteObject: Note):
        self.notebook.append(NoteObject)

    def delete_note(self):
        self.print_notebook()
        print('Введите номер заметки, которую вы хотите удалить: ')
        choise = int(input())
        del self.notebook[choise-1]
        self.print_notebook()

    def print_notebook(self):
        i = 1
        for item in self.notebook:
            if isinstance(item, Note):
                print(i)
                item.print_note()
                i += 1

    def change_note(self):
        self.print_notebook()
        print('Введите номер заметки, которую вы хотите редактировать: ')
        choise = int(input())
        changable_note = self.notebook[choise-1]
        print('Если вы хотите изменить заголовок заметки, нажмите 1')
        print('Если вы хотите изменить содержание заметки, нажмите 2')
        print('Если вы хотите изменить заметку целиком, нажмите 3')
        pick = int(input())
        if isinstance(changable_note, Note):
            match pick:
                case 1:
                    changable_note.set_title()
                    changable_note.set_last_dt()
                case 2:
                    changable_note.set_content()
                    changable_note.set_last_dt()
                case 3:
                    changable_note.set_title()
                    changable_note.set_content()
                    changable_note.set_last_dt()
        self.print_notebook()
