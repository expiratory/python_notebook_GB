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
