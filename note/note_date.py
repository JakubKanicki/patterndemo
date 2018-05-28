from note.note_base import NoteBase


class NoteDate(NoteBase):

    def __init__(self, id=None, text='', date=''):
        NoteBase.__init__(self, 'date', id)
        self.text = text
        self.date = date

    def set_data(self, data):
        self.text = data['text']
        self.date = data['date']

    def get_data(self):
        return {'text': self.text, 'date': self.date}

    def __repr__(self):
        return 'DateNote: %s on %s' % (self.text, self.date)
