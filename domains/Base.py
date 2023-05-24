class Base():
    name: str
    def __init__(self):
        self.name = ""
    def check(self, value):
        return  self.name + " " + value