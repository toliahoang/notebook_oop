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

    def search(self, string):
        return [note for note in self.notes if note.match_search(string)]

    def __repr__(self):
        return self.notes