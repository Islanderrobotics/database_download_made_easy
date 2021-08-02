import os
import zipfile
import pandas as pd
from datetime import date
class Database:
    def __init__(self,API_call):
        os.system(API_call)
        self.name = API_call.split("/")
        self.Open()
        os.remove(self.name[1]+".zip")
    def Open(self):
        self.dataset = []
        with zipfile.ZipFile(self.name[1]+".zip", 'r') as zip:
            filename = zip.namelist()
            zip.extractall()
        newfilename = []
        for i in filename:
            name = i.split(".")[0]
            os.rename(rf"{i}", rf"{name}-{date.today()}.csv")
            newfilename.append(name+"-"+str(date.today())+".csv")
        for i in newfilename:
            self.dataset.append(pd.read_csv(i))
        self.filenames=newfilename
