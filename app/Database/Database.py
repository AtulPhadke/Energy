from Data import Data
import sqlite3
import time
import datetime
import requests
#"(:bool, :time, :place, :plantname, :humidity, :temperature, :wateranalog)"
# NOTE: bool is always '1'
url = "http://192.168.1.24:5263/"
values = {
    "bool": 0,
    "time": 1,
    "place": 2,
    "plantname": 3,
    "humidity": 4,
    "temperature": 5,
    "wateranalog": 6
}
life = 1
previous = {
    "place": 0,
    "plantname": 0,
    "humidity": 0,
    "temperature": 0,
    "wateranalog": 0
}
now = time.time()
future = now + 10
i = 0
humidity = 0
temperature = 0
wateranalog = 0
while(1):
    #time.sleep(0.01)
    r = requests.get(url)
    text = r.text
    if "<p>" in text:
        if i == 0:
            humidity = str(text[50:54])
            if humidity != "None":
                humidity = float(humidity)
                #print(humidity)
        if i == 1:
            temperature = str(text[64:68])
            #print(temperature)
            if temperature != "None": #o/r temperature != "itio":
                temperature = float(temperature)
                #print(temperature)
        if i == 2:
            wateranalog = str(text[78:81])
            if "<" in wateranalog:
                wateranalog = str(text[78:80])
            if wateranalog != "None" or wateranalog != "itio":
                wateranalog = float(wateranalog)
                #print(temperature)

        i = i + 1
        if i == 2:
            i = 0
    new = {
        "place": 0,
        "plantname": 0,
        "humidity": humidity,
        "temperature": temperature,
        "wateranalog": wateranalog
    }
    if time.time() > future:
        for key in new.keys():
            if new[key] != previous[key]:
                print("not matching")
                new1 = Data("1", datetime.datetime.now(), new["place"], new["plantname"], new["humidity"], new["temperature"], new["wateranalog"])
                new1.InsertData()
                future = future + 10
                previous[key] = new[key]
    if life == 0:
        x = Data("1", datetime.datetime.now(), new["place"], new["plantname"], new["humidity"], new["temperature"], new["wateranalog"])
        data = x.GetAllData()
        sum = 0
        average = 0
        i = 0
        for values in data[0:]:
            sum = sum + values[5]
            i = i + 1
            average = sum/i
            print(average)
