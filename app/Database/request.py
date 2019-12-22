import requests

url = "http://192.168.1.24:5263/"
#print(text)
i = 0
while(1):
    r = requests.get(url)
    text = r.text
    if "<p>" in text:
        if i == 0:
            humidity = str(text[50:54])
            if humidity != "None":
                humidity = float(humidity)
                print(humidity)
        if i == 1:
            temperature = str(text[64:68])
            if temperature != "None":
                temperature = float(temperature)
                print(temperature)
        if i == 2:
            wateranalog = str(text[64:68])
            if temperature != "None":
                temperature = float(temperature)
                print(temperature)
        i = i + 1
        if i == 2:
            i = 0


