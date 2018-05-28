import pymongo

from database.database_mongo import DatabaseMongo
from note import note_builder
from note import note_writer
from note.note_simple import NoteSimple


def main():
    print(pymongo.get_version_string())

    dbc = DatabaseMongo('localhost', 27017)

    dbc.add_note('note', {'name': 'hangout', 'desc': 'Just hang out'})
    mod = dbc.add_note('date', {'text': 'Eat shower', 'date': '12018'})
    dbc.add_note('check', {'name': 'Eat', 'what': 'a grue'})

    for nt in dbc.get_all_notes():
        print(nt)
    print()

    note_data = dbc.get_note(mod)['data']
    note_data['text'] = 'Order a rift'; note_data['date'] = '27.05.2018'

    dbc.update_note(mod, note_data)

    notes = []
    notes.append(NoteSimple(text='Walk the cat.'))
    notes.append(NoteSimple(text='Feed the dog.'))
    notes.append(NoteSimple(text='Pet the parrot.'))
    for note in notes:
        note_writer.write_note(dbc, note)

    for nt in dbc.get_all_notes():
        print(nt)

    notes = []
    note_data = dbc.get_all_notes()
    for data in note_data:
        note = note_builder.construct_note(data)
        if note:
            notes.append(note)

    for note in notes:
        print(note)

    dbc.drop_database()


if __name__ == '__main__':
    main()
