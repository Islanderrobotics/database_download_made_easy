import os
import zipfile
import pandas as pd
class Database:
    def __init__(self,API_call, removefile = False):
        self.name = API_call.split("/")
        os.system(API_call)
        with zipfile.ZipFile(self.name[1]+".zip", 'r') as zip:
            self.filename = zip.namelist()
            zip.extractall()
        self.dataset = []
        for i in self.filename:
            self.dataset.append(pd.read_csv(i))
        if(removefile):
            os.remove(self.name[1]+".zip")
            for i in self.filename:
                os.remove(i)