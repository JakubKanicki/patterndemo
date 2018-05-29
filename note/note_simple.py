from note.note_base import NoteBase


class NoteSimple(NoteBase):

    def __init__(self, id=None, text=''):
        NoteBase.__init__(self, NoteSimple.__name__, id)
        self.__text = text

    def set_data(self, data):
        self.__text = data['text']

    def get_data(self):
        return {'text': self.__text}

    def set_text(self, text):
        self.__text = text
        self.__is_dirty = True

    def get_text(self):
        return self.__text

    def __repr__(self):
        return 'SimpleNote: %s' % self.__text
