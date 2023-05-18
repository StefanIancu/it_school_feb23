class Complaint:

    current_id = 0

    def __init__(self, title, text) -> None:
        self.__id = Complaint.current_id
        self.__title = title
        self.__text = text
        self.__resolved = False

        Complaint.current_id += 1

    @property
    def id(self):
        return self.__id
    
    @property
    def text(self):
        return self.__text
    
    @property
    def title(self):
        return self.__title
    
    @property
    def resolved(self):
        return self.__resolved
    
    def mark_as_resolved(self):
        self.__resolved = True

    