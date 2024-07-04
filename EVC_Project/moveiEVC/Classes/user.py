class User:
    def __init__(self, name, number):
        self.UserName = name
        self.UserNumber = number

    def setUserName(self, name):
        self.UserName = name

    def setUserNumber(self, number):
        self.UserNumber = number

    def getUserName(self):
        return self.UserName

    def getUserNumber(self):
        return self.UserNumber
