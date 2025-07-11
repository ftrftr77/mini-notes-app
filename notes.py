notes = []


def delete_note(idx):
    notes.pop(idx)


def save_notes():
    with open("notes.txt", "w") as f:
        f.write("\\n".join(notes))
