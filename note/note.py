import datetime
last_id = 0


class Note():

    def __init__(self, memo, tags = ''):

        self.memo = memo
        self.creation_data = datetime.date.today()
        self.tags = tags
        global last_id
        last_id += 1
        self.id = last_id

    def match_search(self, string):
        return string in self.memo or string in self.tags


    def __repr__(self):
        return f"{self.memo}--{self.tags}"