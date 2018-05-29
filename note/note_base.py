
class NoteBase:

    def __init__(self, type, id):
        self.__type = type
        self.__id = id
        self.__is_dirty = id is None

    def set_data(self, data):
        raise NotImplementedError

    def get_data(self):
        raise NotImplementedError

    def get_type(self):
        return self.__type

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def mark_clean(self):
        self.__is_dirty = False

    def is_dirty(self):
        return self.__is_dirty