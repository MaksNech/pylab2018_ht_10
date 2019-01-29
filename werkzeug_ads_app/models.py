import datetime


class Advertisement():
    def __init__(self, title: str, desc: str):
        """
        Constructor.
        :param title: (str)
        :param desc: (str)
        :return (new Advertisement obj)
        """
        self._title = title
        self._description = desc
        self._created_at = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value: list):
        self._title = value

    @title.deleter
    def title(self):
        del self._title

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value: list):
        self._description = value

    @description.deleter
    def description(self):
        del self._description

    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, value: list):
        self._created_at = value

    @created_at.deleter
    def created_at(self):
        del self._created_at

    def generate_document(self) -> dict:
        """
        Generates document of the object.
        :return: (dict)
        """
        return {'title': self._title, 'desc': self._description, 'created_at': self._created_at}
