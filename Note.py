import datetime as dt


class Note:
    title = ''
    content = ''
    creation_time = dt.datetime.now()
    last_change_time = dt.datetime.now()

    def __init__(self, title='', content='', creation_time=str(dt.datetime.now()), last_change_time=str(dt.datetime.now())):
        self.title = title
        self.content = content
        self.creation_time = dt.datetime.strptime(
            creation_time, '%Y-%m-%d %H:%M:%S.%f')
        self.last_change_time = dt.datetime.strptime(
            last_change_time, '%Y-%m-%d %H:%M:%S.%f')

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

    def set_last_dt(self):
        self.last_change_time = dt.datetime.now()

    def print_note(self):
        print('------------------------------------------------------------------------\n'
              + 'Заметка № ' + str(self.get_id()) + ';\n'
                + 'Заголовок: ' + self.title + ';\n'
                + 'Содержание: ' + self.content + ';\n'
                + 'Дата и время создания: ' + str(self.creation_time) + ';\n'
                + 'Дата и время последнего изменения: ' +
              str(self.last_change_time) + ';\n'
                + '------------------------------------------------------------------------\n'
                + '###')

    def to_string(self):
        return str(self.get_id()) + ';' + self.title + ';' + self.content + ';' + str(self.creation_time) + ';' + str(self.last_change_time)
