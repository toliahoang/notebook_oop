from note.note import Note
from notebook.notebook_file import NoteBook

class Menu():

    def __init__(self):
        notebook  = NoteBook()
        self.choice = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit
        }

    def display_menu(self):
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
        pass
