import io
class DiaryModel(object):
    def __init__(self, text, date):
        self.text = text
        self.date = date
    def SaveInfo(self):
        with open(self.date+".txt", "w+") as self.f:
            self.f.write(str(self.text))
            self.f.close()          