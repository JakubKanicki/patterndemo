from note.note_base import NoteBase


class NoteSimple(NoteBase):

    def __init__(self, text=''):
        super(NoteSimple, self).__init__('simple')
        self.text = text

    def set_data(self, data):
        self.text = data['text']

    def get_data(self):
        return {'text': self.text}

    def __repr__(self):
        return 'SimpleNote: %s' % self.text