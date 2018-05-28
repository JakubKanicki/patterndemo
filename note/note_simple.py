from note.note_base import NoteBase


class NoteSimple(NoteBase):

    def __init__(self, id=None, text=''):
        NoteBase.__init__(self, 'simple', id)
        self._text = text

    def set_data(self, data):
        self._text = data['text']

    def get_data(self):
        return {'text': self._text}

    def set_text(self, text):
        self._text = text
        self._is_dirty = True

    def get_text(self):
        return self._text

    def __repr__(self):
        return 'SimpleNote: %s' % self._text
