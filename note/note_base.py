
class NoteBase:

    def __init__(self, type, id):
        self.type = type
        self.id = id

    def set_data(self, data):
        pass

    def get_data(self):
        pass

    def get_type(self):
        return self.type

    def get_id(self):
        return self.id
