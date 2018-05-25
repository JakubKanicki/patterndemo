import pymongo
from database.database_mongo import DatabaseMongo
from note.note_simple import NoteSimple


def main():
    print(pymongo.get_version_string())

    db = DatabaseMongo('localhost', 27017)

    db.add_note('note', {'name': 'hangout', 'desc': 'Just hang out'})
    mod = db.add_note('reminder', {'name': 'Remember!', 'desc': 'Eat shower', 'date': '12018'})
    db.add_note('check', {'name': 'Eat', 'what': 'a grue'})

    for nt in db.get_all_notes():
        print(nt)
    print()

    note_data = db.get_note(mod)['data']
    note_data['desc'] = 'Order a rift'; note_data['date'] = '24.05.2018'

    db.update_note(mod, {'name': note_data})

    note = NoteSimple('Walk the cat')
    id = db.add_note(note.get_type(), note.get_data())

    for nt in db.get_all_notes():
        print(nt)

    note_temp = db.get_note(id)
    notte = NoteSimple()
    notte.set_data(note_temp['data'])
    print(str(notte))

    db.drop_database_lol()


main()