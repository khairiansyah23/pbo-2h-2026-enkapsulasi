from datetime import datetime

class Book:
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author
        self.last_updated = datetime.now()

def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def set_title(self, new_title):
        self.__title = new_title
