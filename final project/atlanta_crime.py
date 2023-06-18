import pandas as pd
import numpy as np
import random
from datetime import datetime
class DP:
    def __init__(self):

        self.df1=pd.DataFrame()
    def delLocCol(self):
        self.df1.drop('location', inplace=True, axis=1)

    def synthesizeColumns(self):
        self.df1=pd.read_csv(r"./atlcrime.csv")
        lenofSample=len(self.df1.index)
        agegroup=["0-18","18-35","35-50","50-65","65-80","80-95"]
        sex=["Male","Female"]
        race=["White","Non-White"]
        lst1=[]
        lst2=[]
        lst3=[]
        for i in range(lenofSample):
            j1=random.choice(agegroup)
            lst1.append(j1)
            j2=random.choice(sex)
            lst2.append(j2)
            j3=random.choice(race)
            lst3.append(j3)

        ser1=pd.Series(lst1)
        ser2=pd.Series(lst2)
        ser3=pd.Series(lst3)

        self.df1["victim-age-group"]=ser1
        self.df1["victim-sex"] = ser2
        self.df1["victim-race"]=ser3
    def dateProc(self):
        dateCol=self.df1["date"]
        print(dateCol)
        lst=[]
        for i,j in self.df1.iterrows():
            dt=datetime.strptime(j["date"],"%m/%d/%Y")
            st=dt.strftime("%m/%Y")
            lst.append(st)
        ser=pd.Series(lst)
        self.df1["date"]=ser
        print(self.df1["date"])
    def latlongProc(self):
        lst1=[]
        lst2=[]
        for i, j in self.df1.iterrows():
            print(j["lat"])
            latrnd=round(float(j["lat"]),2)
            longrnd=round(float(j["long"]),2)
            lst1.append(latrnd)
            lst2.append(longrnd)
        ser1=pd.Series(lst1)
        ser2=pd.Series(lst2)
        self.df1['lat']=ser1
        self.df1['long']=ser2
        print(self.df1)
        self.df1.to_csv("atlcrimeDP2.csv", index=False)



obj=DP()
obj.synthesizeColumns()
obj.delLocCol()
obj.dateProc()
obj.latlongProc()

