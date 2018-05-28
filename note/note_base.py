
class NoteBase:

    def __init__(self, type, id):
        self._type = type
        self._id = id
        self._is_dirty = id is None

    def set_data(self, data):
        pass

    def get_data(self):
        pass

    def get_type(self):
        return self._type

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id

    def mark_clean(self):
        self._is_dirty = False

    def is_dirty(self):
        return self._is_dirty