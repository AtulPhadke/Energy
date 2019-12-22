import sqlite3
conn = sqlite3.connect('/Users/atulphadke/Documents/Energy/plantdata.db')
c = conn.cursor()
class Data:
    def __init__(self, bool, time, place, plantname, humidity, temperature, wateranalog):
        self.humidity = humidity
        self.temperature = temperature
        self.wateranalog = wateranalog
        self.bool = '1'
        self.time = time
        self.place = place
        self.plantname = plantname
    def InsertData(self):
        c.execute("INSERT INTO plantdata VALUES (:bool, :time, :place, :plantname, :humidity, :temperature, :wateranalog)", (self.bool, self.time, self.place, self.plantname, self.humidity, self.temperature, self.wateranalog))
        print("Inserted")
        conn.commit()
        #conn.close()
    def GetOneData(self, array):
        c.execute("SELECT * FROM plantdata WHERE bool='1'")
        print(c.fetchall()[-1][array])
        conn.commit()
        #conn.close()
    def GetAllData(self):
        c.execute("SELECT * FROM plantdata WHERE bool='1'")
        #print(c.fetchall())
        data = c.fetchall()
        conn.commit()
        return data
        #conn.close()
    def GetManyData(self, number):
        c.execute("SELECT * FROM plantdata WHERE bool='1'")
        print(c.fetchall()[-number:])
        conn.commit()
        #conn.close()
    def runDataBase(self, array):
        self.InsertData()
        self.GetOneData(array)
        conn.commit()
        #conn.close()
