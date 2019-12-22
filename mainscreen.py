import pygame
import time
import datetime
import requests
from pprint import pprint
import pygame
from pygame.locals import *
import random
from Data import Data
from OpenGL.GL import *
from OpenGL.GLU import *
from ControlPanelClass import ControlPanel_main


imageDirectory = "/Users/atulphadke/Documents/Energy/images/"
fontDirectory  = "/Users/atulphadke/Documents/Energy/fonts/"
previousRes   = 0
newRes        = 0
previousImage = imageDirectory + "beginning.png"
newImage      = imageDirectory + "beginning.png"
firstTime  = 0

pygame.init()
screen = pygame.display.set_mode((1024, 600))
rectBlack = pygame.Rect(0, 0, 1024, 600)
clock = pygame.time.Clock()

def ControlPanelButton(imageDirectory, fontDirectory, screen):
    x, y = pygame.mouse.get_pos()
    if x >= 585 and x <= 775 and y <= 575 and y >= 515:
        button = pygame.image.load(imageDirectory + "HoverControlPanel.png")
        button = pygame.transform.scale(button, (275, 200))
        screen.blit(button, (550, 500))
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("a")
            verticies = (
            (1, -1, -1),
            (1, 1, -1),
            (-1, 1, -1),
            (-1, -1, -1),
            (1, -1, 1),
            (1, 1, 1),
            (-1, -1, 1),
            (-1, 1, 1)
            )
            edges = (
            (0,1),
            (0,3),
            (0,4),
            (2,1),
            (2,3),
            (2,7),
            (6,3),
            (6,4),
            (6,7),
            (5,1),
            (5,4),
            (5,7)
            )
            display = (1024,600)
            screen = pygame.display.set_mode((1024,600), DOUBLEBUF|OPENGL)
            gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
            glTranslatef(0.0,0.0, -5)
            speed = 1
            i = 0
            v = 0
            change = 1
            maxRotations = 9
            minRotations = -9
            fin = False
            while True:
                if i == 10:
                    speed = speed - change
                    i = 0
                if speed == minRotations:
                    change = -1
                if speed == maxRotations:
                    change = 1
                glRotatef(speed, 0, 2, 0)
                glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
                glBegin(GL_LINES)
                for edge in edges:
                    for vertex in edge:
                        glVertex3fv(verticies[vertex])
                pygame.display.flip()
                #pygame.time.wait(10)
                i = i + 1
                v = v + 5
                if v == 1500:
                    v = 0
                    screen = pygame.display.set_mode((1024, 600))
                    fin = True
                    return fin
    else:
        button = pygame.image.load(imageDirectory + "ControlPanel.png")
        button = pygame.transform.scale(button, (275, 200))
        screen.blit(button, (550, 500))

def ResetButton(imageDirectory, fontDirectory):
    x, y = pygame.mouse.get_pos()
    if x >= 785 and x <= 975 and y <= 575 and y >= 515:
        button = pygame.image.load(imageDirectory + "HoverRoundedRectangle.png")
        button = pygame.transform.scale(button, (275, 200))
        screen.blit(button, (750, 500))
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("a")
            verticies = (
            (1, -1, -1),
            (1, 1, -1),
            (-1, 1, -1),
            (-1, -1, -1),
            (1, -1, 1),
            (1, 1, 1),
            (-1, -1, 1),
            (-1, 1, 1)
            )

            edges = (
            (0,1),
            (0,3),
            (0,4),
            (2,1),
            (2,3),
            (2,7),
            (6,3),
            (6,4),
            (6,7),
            (5,1),
            (5,4),
            (5,7)
            )
            def Cube():
                glBegin(GL_LINES)
                for edge in edges:
                    for vertex in edge:
                        glVertex3fv(verticies[vertex])
                glEnd()
            def main():
                display = (1024,600)
                screen = pygame.display.set_mode((1024,600), DOUBLEBUF|OPENGL)
                gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
                glTranslatef(0.0,0.0, -5)
                speed = 1
                i = 0
                v = 0
                change = 1
                maxRotations = 9
                minRotations = -9
                fin = False
                while True:
                    if i == 10:
                        speed = speed - change
                        i = 0
                    if speed == minRotations:
                        change = -1
                    if speed == maxRotations:
                        change = 1
                    glRotatef(speed, 0, 2, 0)
                    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
                    Cube()
                    pygame.display.flip()
                    #pygame.time.wait(10)
                    i = i + 1
                    v = v + 5
                    if v == 500:
                        v = 0
                        screen = pygame.display.set_mode((1024, 600))
                        fin = True
                        return fin
            main()
            finish = main()
            if finish == True:
                return finish
    else:
        button = pygame.image.load(imageDirectory + "Rounded_Rectangle.png")
        button = pygame.transform.scale(button, (275, 200))
        screen.blit(button, (750, 500))
def Megamanand10800A(imageDirectory, fontDirectory):
    megaman = imageDirectory + "sprite_09.png"
    loadingicons = pygame.image.load(megaman)
    loadingicons = pygame.transform.scale(loadingicons, (200, 200))
    screen.blit(loadingicons, (780, 180))
    Team = pygame.font.Font(fontDirectory + 'BebasNeueBold.ttf', 90)
    Teams = Team.render("10800A", 40, (255, 255, 255))
    screen.blit(Teams, (770, 380))
def CarbonDioxide(maximum, imageDirectory, fontDirectory):
    H20 = 500
    if H20 <= (maximum/30):
        image = imageDirectory + "frame_00_delay-0.33s.png"

    elif (maximum/30)*2 <= H20 <= (maximum/30)*3:
        image = imageDirectory + "frame_01_delay-0.33s.png"

    elif (maximum/30)*3 <= H20 <= (maximum/30)*4:
        image = imageDirectory + "frame_02_delay-0.33s.png"

    elif (maximum/30)*4 <= H20 <= (maximum/30)*5:
        image = imageDirectory + "frame_03_delay-0.33s.png"

    elif (maximum/30)*5 <= H20 <= (maximum/30)*6:
        image = imageDirectory + "frame_04_delay-0.33s.png"

    elif (maximum/30)*6 <= H20 <= (maximum/30)*7:
        image = imageDirectory + "frame_05_delay-0.33s.png"

    elif (maximum/30)*7 <= H20 <= (maximum/30)*8:
        image = imageDirectory + "frame_06_delay-0.33s.png"

    elif (maximum/30)*8 <= H20 <= (maximum/30)*9:
        image = imageDirectory + "frame_07_delay-0.33s.png"

    elif (maximum/30)*9 <= H20 <= (maximum/30)*10:
        image = imageDirectory + "frame_08_delay-0.33s.png"

    elif (maximum/30)*10 <= H20 <= (maximum/30)*11:
        image = imageDirectory + "frame_09_delay-0.33s.png"

    elif (maximum/30)*11 <= H20 <= (maximum/30)*12:
        image = imageDirectory + "frame_10_delay-0.33s.png"

    elif (maximum/30)*12 <= H20 <= (maximum/30)*13:
        image = imageDirectory + "frame_11_delay-0.33s.png"

    elif (maximum/30)*13 <= H20 <= (maximum/30)*14:
        image = imageDirectory + "frame_12_delay-0.33s.png"

    elif (maximum/30)*14 <= H20 <= (maximum/30)*15:
        image = imageDirectory + "frame_13_delay-0.33s.png"

    elif (maximum/30)*15 <= H20 <= (maximum/30)*16:
        image = imageDirectory + "frame_14_delay-0.33s.png"

    elif (maximum/30)*16 <= H20 <= (maximum/30)*17:
        image = imageDirectory + "frame_15_delay-0.33s.png"

    elif (maximum/30)*17 <= H20 <= (maximum/30)*18:
        image = imageDirectory + "frame_16_delay-0.33s.png"

    elif (maximum/30)*18 <= H20 <= (maximum/30)*19:
        image = imageDirectory + "frame_17_delay-0.33s.png"

    elif (maximum/30)*19 <= H20 <= (maximum/30)*20:
        image = imageDirectory + "frame_18_delay-0.33s.png"

    elif (maximum/30)*20 <= H20 <= (maximum/30)*21:
        image = imageDirectory + "frame_19_delay-0.33s.png"

    elif (maximum/30)*21 <= H20 <= (maximum/30)*22:
        image = imageDirectory + "frame_20_delay-0.33s.png"

    elif (maximum/30)*22 <= H20 <= (maximum/30)*23:
        image = imageDirectory + "frame_21_delay-0.33s.png"

    elif (maximum/30)*23 <= H20 <= (maximum/30)*24:
        image = imageDirectory + "frame_22_delay-0.33s.png"

    elif (maximum/30)*24 <= H20 <= (maximum/30)*25:
        image = imageDirectory + "frame_23_delay-0.33s.png"

    elif (maximum/30)*25 <= H20 <= (maximum/30)*26:
        image = imageDirectory + "frame_24_delay-0.33s.png"

    elif (maximum/30)*26 <= H20 <= (maximum/30)*27:
        image = imageDirectory + "frame_25_delay-0.33s.png"

    elif (maximum/30)*27 <= H20 <= (maximum/30)*28:
        image = imageDirectory + "frame_26_delay-0.33s.png"

    elif (maximum/30)*28 <= H20 <= (maximum/30)*29:
        image = imageDirectory + "frame_27_delay-0.33s.png"

    elif (maximum/30)*29 <= H20 >= maximum:
        image = imageDirectory + "frame_28_delay-0.33s.png"

    elif H20 >= maximum:
        image = imageDirectory + "frame_29_delay-0.33s.png"

    loadingicon = pygame.image.load(image)
    loadingicon = pygame.transform.scale(loadingicon, (200, 200))
    screen.blit(loadingicon, (20, 450))

def GetTempData(imageDirectory, fontDirectory):
    x = datetime.datetime.now()
    url = 'http://openweathermap.org/data/2.5/weather?q={}&appid=b6907d289e10d714a6e88b30761fae22'.format("Nashua")
    res = requests.get(url)
    data = res.json()
    temp = data['main']['temp']
    templow = data['main']['temp_min']
    templow = templow*(9/5) + 32
    temphigh = data['main']['temp_max']
    temphigh = temphigh*(9/5) + 32
    weathers = data['weather'][0]['main']
    temp = temp*(9/5) + 32
    return temp, templow, temphigh, weathers

def GetWeatherTempData(temp, templow, temphigh, weathers, imageDirectory, fontDirectory):
        x = datetime.datetime.now()
        if temp <= 40:
            status = 'Cold'
            Status = pygame.font.Font(fontDirectory + 'NanumGothic-Regular.ttf', 30)
            ColdHotMild = Status.render(status, 10, (255, 255, 255))
            #screen.blit(s, (20, 100))
        elif temp >= 80:
            status = 'Hot'
            Status = pygame.font.Font(fontDirectory + 'NanumGothic-Regular.ttf', 30)
            ColdHotMild = Status.render(status, 10, (255, 255, 255))
            #screen.blit(s, (20, 100))
        else:
            status = 'Mild'
            Status = pygame.font.Font(fontDirectory + 'NanumGothic-Regular.ttf', 30)
            ColdHotMild = Status.render(status, 10, (255, 255, 255))
            #screen.blit(s, (20, 100))
        if weathers == 'Rain':
            weathericon = pygame.image.load(imageDirectory + "rain.png")
            Wweathericon = pygame.transform.scale(weathericon, (100, 100))
            #screen.blit(weathericon, (220, 10))
            if 6 <= int(x.strftime("%H")) <= 16:
                weathericon = pygame.image.load(imageDirectory + "Sunny.png")
                DNweathericon = pygame.transform.scale(weathericon, (100, 100))
                #screen.blit(weathericon, (340, 10))
            elif int(x.strftime("%H")) >= 17 or int(x.strftime("%H")) <= 5:
                weathericon = pygame.image.load(imageDirectory + "Moon1.png")
                DNweathericon = pygame.transform.scale(weathericon, (100, 100))
                #screen.blit(weathericon, (340, 10))
        elif weathers == 'Clouds':
            weathericon = pygame.image.load(imageDirectory + "clouds.png")
            Wweathericon = pygame.transform.scale(weathericon, (100, 100))
            #screen.blit(weathericon, (220, 10))
            if 6 <= int(x.strftime("%H")) <= 16:
                weathericon = pygame.image.load(imageDirectory + "Sunny.png")
                DNweathericon = pygame.transform.scale(weathericon, (100, 100))
                #screen.blit(weathericon, (340, 10))
            elif int(x.strftime("%H")) >= 17 or int(x.strftime("%H")) <= 5:
                weathericon = pygame.image.load(imageDirectory + "Moon1.png")
                DNweathericon = pygame.transform.scale(weathericon, (100, 100))
                #screen.blit(weathericon, (340, 10))
        elif weathers == 'Snow':
            weathericon = pygame.image.load(imageDirectory + "snow.png")
            Wweathericon = pygame.transform.scale(weathericon, (100, 100))
            #screen.blit(weathericon, (220, 10))
            if 6 <= int(x.strftime("%H")) <= 16:
                weathericon = pygame.image.load(imageDirectory + "Sunny.png")
                DNweathericon = pygame.transform.scale(weathericon, (100, 100))
                #screen.blit(weathericon, (340, 10))
            elif int(x.strftime("%H")) >= 17 or int(x.strftime("%H")) <= 5:
                weathericon = pygame.image.load(imageDirectory + "Moon1.png")
                DNweathericon = pygame.transform.scale(weathericon, (100, 100))
                #screen.blit(weathericon, (340, 10))
        elif weathers == 'Clear':
            weathericon = pygame.image.load(imageDirectory + "Clear.png")
            Wweathericon = pygame.transform.scale(weathericon, (100, 100))
            #screen.blit(weathericon, (220, 10))
            if 6 <= int(x.strftime("%H")) <= 16:
                weathericon = pygame.image.load(imageDirectory + "Sunny.png")
                DNweathericon = pygame.transform.scale(weathericon, (100, 100))
                #screen.blit(weathericon, (340, 10))
            elif int(x.strftime("%H")) >= 17 or int(x.strftime("%H")) <= 5:
                weathericon = pygame.image.load(imageDirectory + "Moon1.png")
                DNweathericon = pygame.transform.scale(weathericon, (100, 100))
                #screen.blit(weathericon, (340, 10))
        return DNweathericon, Wweathericon, ColdHotMild


def displayWeatherData(imageDirectory, fontDirectory):
        temperature = pygame.font.Font(fontDirectory + 'NanumGothic-Regular.ttf', 75)
        Temps = temperature.render(str(int(temp)) + " F", 50, (255, 255, 255))
        temperaturelow = pygame.font.Font(fontDirectory + 'NanumGothic-Regular.ttf', 20)
        low = temperaturelow.render(str(int(templow))+ " F", 25, (255, 255, 255))
        temperaturehigh = pygame.font.Font(fontDirectory + 'NanumGothic-Regular.ttf', 20)
        high = temperaturehigh.render(str(int(temphigh))+ " F", 25, (255, 255, 255))
        screen.blit(Temps, (20, 20))
        screen.blit(low, (330, 120))
        screen.blit(high, (400, 120))
        screen.blit(DNweathericon, (340, 10))
        screen.blit(Wweathericon, (220, 10))
        screen.blit(ColdHotMild, (20, 100))

def Title(imageDirectory, fontDirectory):
    Title = pygame.font.Font(fontDirectory + 'NanumGothic-Regular.ttf', 25)
    title = Title.render("Battery Life", 50, (255, 255, 255))
    screen.blit(title, (250, 525))


def Time(imageDirectory, fontDirectory):
    z = datetime.datetime.now()
    screen.fill((0,0,0))
    Time = pygame.font.Font(fontDirectory + 'NanumGothic-Regular.ttf', 50)
    Time1 = pygame.font.Font(fontDirectory + 'NanumGothic-Regular.ttf', 25)
    Time2 = pygame.font.Font(fontDirectory + 'NanumGothic-Regular.ttf', 25)
    y = Time.render(z.strftime("%H:%M:%S"), 50, (255, 255, 255))
    q = Time1.render(z.strftime("%b %d %Y"), 50, (255, 255, 255))
    screen.blit(y, (780, 20))
    screen.blit(q, (790, 80))
    if 6 <= int(z.strftime("%H")) <= 13:
            d = Time2.render("Good Morning!", 50, (255, 255, 255))
            screen.blit(d, (790, 110))
    if 14 <= int(z.strftime("%H")) <= 16:
            d = Time2.render("Good Afternoon!", 50, (255, 255, 255))
            screen.blit(d, (790, 110))
    if int(z.strftime("%H")) >= 17 or int(z.strftime("%H")) <= 5:
            d = Time2.render("Good Evening!", 50, (255, 255, 255))
            screen.blit(d, (790, 110))

finished = False

url = 'http://openweathermap.org/data/2.5/weather?q={}&appid=b6907d289e10d714a6e88b30761fae22'.format("Nashua")

i = 0
previous_temp = 0.0
previous_weathers = "now"
previous_time = 0
previous_temp = 0.0
previous_tempLow = 0.0
previous_tempHigh = 0.0
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
temperatures = 0
wateranalog = 0

## create control Panel object.
#controlPanel_new = ControlPanel_main(previousImage, newImage)
previousRes   = 0
newRes        = 0
previousImage = imageDirectory + "beginning.png"
newImage      = imageDirectory + "beginning.png"
firstTime  = 0
controlPanel_new = ControlPanel_main(previousImage, newImage)

while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    finished = True
        if i == 0:
            temp, templow, temphigh, weathers = GetTempData(imageDirectory, fontDirectory)
            DNweathericon, Wweathericon, ColdHotMild = GetWeatherTempData(temp, templow, temphigh, weathers, imageDirectory, fontDirectory)
        Time(imageDirectory, fontDirectory)
        Title(imageDirectory, fontDirectory)
        new_time = int(time.time())
        if new_time - previous_time > 60:
            #print("timer exceeded")
            #print(new_time)
            temp, templow, temphigh, weathers = GetTempData(imageDirectory, fontDirectory)
            if temp != previous_temp \
               or templow != previous_tempLow \
               or temphigh != previous_tempHigh \
               or weathers != previous_weathers:
                #print("temp info is different")
                DNweathericon, Wweathericon, ColdHotMild = GetWeatherTempData(temp, templow, temphigh, weathers, imageDirectory, fontDirectory)
                previous_temp = temp
                previous_temLow = templow
                previous_tempHigh = temphigh
                previous_weathers = weathers
            previous_time = new_time
        displayWeatherData(imageDirectory, fontDirectory)
        CarbonDioxide(1000, imageDirectory, fontDirectory)
        Megamanand10800A(imageDirectory, fontDirectory)
        ResetButton(imageDirectory, fontDirectory)
        ControlPanelButton(imageDirectory, fontDirectory, screen)
        finish = ControlPanelButton(imageDirectory, fontDirectory, screen)
        #print("hello" + str(finish))
        r = requests.get("http://192.168.1.24:5263/")
        text = r.text
        if "<p>" in text:
            if i == 0:
                humidity = str(text[50:54])
                if humidity != "None":
                    humidity = float(humidity)
                    #print(humidity)
            if i == 1:
                temperatures = str(text[64:68])
                #print(temperature)
                if temperatures != "None": #o/r temperature != "itio":
                    temperatures = float(temperatures)
                    #print(temperature)
            if i == 2:
                wateranalog = str(text[78:81])
                if "<" in wateranalog:
                    print("<")
                    wateranalog = str(text[78:79])
                if wateranalog != "None": # or wateranalog != "itio":
                    wateranalog = float(wateranalog)
                    #print(temperature)

            i = i + 1
            if i == 2:
                i = 0
        new = {
            "place": 0,
            "plantname": 0,
            "humidity": humidity,
            "temperature": temperatures,
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
        if finish == True:
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        finished = True
                if firstTime == 0:
                    newRes, newImage = controlPanel_new.ControlPanel(event, previousRes)
                    firstTime = firstTime + 1
                    if previousRes != newRes:
                        previousRes = newRes
                        previousImage = newImage
                if event.type == pygame.MOUSEBUTTONDOWN:
                    newRes, newImage = controlPanel_new.ControlPanel(event, previousRes)
                    if previousRes != newRes:
                        previousRes = newRes
                        previousImage = newImage
                fini = controlPanel_new.Arrowbutton(event, screen)
                if fini == False:
                    finish = False
                    break
                pygame.display.flip()

        i = i + 1
        pygame.display.update()
        clock.tick(60)
