import datetime as dt

class Note:
    title = ''
    content = ''
    creation_time = dt.datetime.now()
    last_change_time = dt.datetime.now()

    def __init__(self):
        pass

    def get_title(self):
        return self.title

    def get_content(self):
        return self.content

    def get_id(self):
        return id(self)

    def set_title(self):
        self.title = str(input('Введите заголовок заметки: '))

    def set_content(self):
        self.content = str(input('Введите содержание заметки: '))

    def get_dt(self):
        return self.creation_time

    def get_last_dt(self):
        return self.last_change_time

    def print_note(self):
        print('------------------------------------------------------------------------' + '\n'\
              + 'Заметка № ' + str(self.get_id()) + ';\n'\
              + 'Заголовок: ' + self.title + ';\n'\
              + 'Содержание: ' + self.content + ';\n'\
              + 'Дата и время создания: ' + str(self.creation_time) + ';\n'\
              + 'Дата и время последнего изменения: ' + str(self.last_change_time) + ';\n'\
              + '------------------------------------------------------------------------\n'\
              + '###')
    
