import pymongo


class DatabaseMongo:

    def __init__(self, ip, port):
        self.conn = pymongo.MongoClient(ip, port)

    def add_note(self, name):
        self.conn.todo.notes.insert_one({'name': name})

    def update_note(self, name, new_name):
        self.conn.todo.notes.update_one({'name': name}, {'$set': {'name': new_name}})

    def get_note(self, name):
        return self.conn.todo.notes.find_one({'name': name})

    def get_all_notes(self):
        return self.conn.todo.notes.find()

    def drop_database_lol(self):
        self.conn.drop_database('todo')