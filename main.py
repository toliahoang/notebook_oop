from note.note import Note
from notebook.notebook_file import NoteBook
import sys


class Menu():

    def __init__(self):
        self.notebook  = NoteBook()
        self.choice = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit
        }

    @staticmethod
    def display_menu():
        print("""
            "1": show_notes,
            "2": search_notes,
            "3": add_note,
            "4": modify_note,
            "5": quit""")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter option: ")
            action = self.choice.get(choice)
            if action:
                action()
            else:
                print("{} is not a valid choice".format(choice))

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print(f"'note_id':{note.id}--'tags':{note.tags}--'memo':{note.memo}")

    def search_notes(self):
        string = input("Enter string for searching: ")
        print(self.notebook.search(string))
        return self.notebook.search(string)

    def add_note(self):
        try:
            memo = input("Enter new memo: ")
            tags = input("Enter new tags: ")
        except Exception as e:
            print(e)
        new_note = self.notebook.new_note(memo, tags)
        return new_note

    def modify_note(self):

        try:
            note_id = int(input("Enter note_id: "))
            memo = input("Enter new memo: ")
            tags = input("Enter new tags: ")
        except Exception as e:
            print(e)
        assert note_id > 0, "note id should > 0"
        self.notebook.modify_tags(note_id - 1, tags)
        self.notebook.modify_memo(note_id - 1,memo)
        return self.notebook.notes

    @staticmethod
    def quit():
        print("system exits")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()