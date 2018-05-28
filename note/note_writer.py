

def write_note(dbc, note):
    if note.get_id():
        dbc.update_note(note.get_id(), note.get_data())
    else:
        inserted_id = dbc.add_note(note.get_type(), note.get_data())
        note.set_id(inserted_id)
