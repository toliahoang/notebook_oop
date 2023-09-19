from note.note import Note

class NoteBook():
    def __init__(self):
        self.notes = []

    def search(self, string):
        return string in self.notes

    def new_note(self, memo, tags):
        new_note = Note(memo, tags)
        self.notes.append(new_note)
        return self.notes


    def modify_memo(self, note_id, memo):
        temp_note = self.notes[note_id]
        temp_note.memo = memo
        return self.notes


    def modify_tags(self, note_id, tags):
        temp_note = self.notes[note_id]
        temp_note.tags = tags
        return self.notes



create_notebook = NoteBook()
get_note = create_notebook.new_note("hi","tw")
print(get_note)
note1 = create_notebook.modify_memo(0,"italy")
print(note1)

