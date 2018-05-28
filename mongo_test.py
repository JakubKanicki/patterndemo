import pymongo

from database.database_mongo import DatabaseMongo
from note import note_builder
from note import note_writer
from note.note_simple import NoteSimple


def main():
    print(pymongo.get_version_string())

    dbc = DatabaseMongo('localhost', 27017)

    dbc.add_note('note', {'name': 'hangout', 'desc': 'Just hang out'})
    mod = dbc.add_note('reminder', {'name': 'Remember!', 'desc': 'Eat shower', 'date': '12018'})
    dbc.add_note('check', {'name': 'Eat', 'what': 'a grue'})

    for nt in dbc.get_all_notes():
        print(nt)
    print()

    note_data = dbc.get_note(mod)['data']
    note_data['desc'] = 'Order a rift'; note_data['date'] = '27.05.2018'

    dbc.update_note(mod, {'name': note_data})

    note = NoteSimple(text='Walk the cat.')
    note_writer.write_note(dbc, note)

    for nt in dbc.get_all_notes():
        print(nt)

    note_entry = dbc.get_note(note.get_id())
    note_test = note_builder.construct_note(note_entry)
    print(str(note_test))

    dbc.drop_database()


if __name__ == '__main__':
    main()
