import pymongo


class DatabaseMongo:

    def __init__(self, ip, port):
        self.conn = pymongo.MongoClient(ip, port)

    def add_note(self, type, data):
        return self.conn.todo.notes.insert_one({'type': type, 'data': data}).inserted_id

    def update_note(self, id, data):
        self.conn.todo.notes.update_one({'_id': id}, {'$set': {'data': data}})

    def get_note(self, id):
        return self.conn.todo.notes.find_one({'_id': id})

    def get_all_notes(self):
        return self.conn.todo.notes.find()

    def drop_database(self):
        self.conn.drop_database('todo')
