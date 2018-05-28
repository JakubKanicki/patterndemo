from note.note_base import NoteBase


class NoteDate(NoteBase):

    def __init__(self, id=None, text='', date=''):
        NoteBase.__init__(self, 'date', id)
        self._text = text
        self._date = date

    def set_data(self, data):
        self._text = data['text']
        self._date = data['date']

    def get_data(self):
        return {'text': self._text, 'date': self._date}

    def set_text(self, text):
        self._text = text
        self._is_dirty = True

    def get_text(self):
        return self._text

    def set_date(self, date):
        self._date = date
        self._is_dirty = True

    def get_date(self):
        return self._date

    def __repr__(self):
        return 'DateNote: %s on %s' % (self._text, self._date)
