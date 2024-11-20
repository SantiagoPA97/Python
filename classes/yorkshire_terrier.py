from classes.dog import Dog


class YorkshireTerrier(Dog):
    def __init__(self, name: str):
        super().__init__(name, "Yorkshire Terrier", 0, "Claudia")
        self._owner = "Claudia"

    @property
    def ownerprop(self):
        return self._owner

    @ownerprop.setter
    def ownerprop(self, owner: str):
        self._owner = owner
        print("Owner has been updated")
