from Note import Note
from Notebook import Notebook


class ImportExport:

    def __init__(self):
        pass

    def export_note(self, notebook: Notebook):
        with open('save.csv', 'a+', encoding='UTF-8') as file:
            for note in notebook.get_notebook():
                if isinstance(note, Note):
                    file.write(note.to_string() + ';\n')

    def import_note(self, notebook: Notebook):
        with open('load.csv', 'r', encoding='UTF-8') as file:
            str_arr = file.readlines()
            for line in str_arr:
                item = line.split(';')
                note = Note(item[1], item[2], item[3], item[4])
                notebook.add_note(note)
            notebook.get_notebook().sort(key=Note.get_dt)
            notebook.print_notebook()
