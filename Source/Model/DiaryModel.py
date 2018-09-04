import io
class DiaryModel(object):
    def __init__(self, text, date):
        self.text = text
        self.date = date
    def SaveInfo(self):
        f = open(self.date+".txt", "w+")
        f.write(self.text)       
        f.close()