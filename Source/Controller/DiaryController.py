import sys
import os.path
sys.path.append("..")
from Model.DiaryModel import *
class DiaryController(object):
    def __init__(self):
        pass
    def checkInfo(self, text, date):
        if os.path.isfile("./%s.txt"%date):
            archivo_texto=open("%s.txt"%date,"r")
            texto = archivo_texto.read()
            return texto
            archivo_texto.close()
        else:
            diary = DiaryModel(text,date)
            diary.SaveInfo()