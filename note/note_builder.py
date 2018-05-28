from note.note_date import NoteDate
from note.note_simple import NoteSimple

note_classes = {
    'simple': NoteSimple,
    'date': NoteDate
}


def construct_note(note_data):
    id = note_data['_id']
    type = note_data['type']
    data = note_data['data']

    if type not in note_classes:
        return None

    note = note_classes[type](id=id)
    note.set_data(data)

    return note
