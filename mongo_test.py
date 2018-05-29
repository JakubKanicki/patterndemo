import pymongo

from database.database_mongo import DatabaseMongo
from note import note_builder
from note import note_writer
from note.note_date import NoteDate
from note.note_simple import NoteSimple


def main():
    print(pymongo.get_version_string())

    dbc = DatabaseMongo('localhost', 27017)

    dbc.add_note('note', {'name': 'hangout', 'desc': 'Just hang out'})
    mod_id = dbc.add_note('date', {'name': 'Remember!', 'text': 'Eat shower', 'date': '12018'})
    dbc.add_note('check', {'name': 'Eat', 'what': 'a grue'})

    for nt in dbc.get_all_notes():
        print(nt)
    print()

    note = note_builder.construct_note(dbc.get_note(mod_id))
    note.set_text('Order a rift')
    note.set_date('27.05.2018')
    note_writer.write_note(dbc, note)

    notes = [
        NoteSimple(text='Walk the cat.'),
        NoteSimple(text='Feed the dog.'),
        NoteDate(text='Receive the rift', date='30.05.2018'),
        NoteSimple(text='Pet the parrot.'),
    ]

    for note in notes:
        note_writer.write_note(dbc, note)

    for nt in dbc.get_all_notes():
        print(nt)
    print()

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
