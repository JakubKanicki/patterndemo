
class NoteBase:

    def __init__(self, type):
        self.type = type

    def get_type(self):
        return self.type

    def set_data(self, data):
        pass

    def get_data(self):
        pass

    @staticmethod
    def construct_note(note_data):
        id = note_data['id']
        type = note_data['type']
        data = note_data['data']

        # TODO

