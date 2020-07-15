def echo():
    return "echo"


class MyClass:
    def __init__(self):
        self.name = ""
        self.number = 0
        self.arr = [
            {"a": 1, "b": 1},
            {"a": 2, "b": 12},
        ]

    def setParam(self):
        self.name = "hogehoge"
        self.number = 888

    def getProperty(self):
        return self.__dict__

