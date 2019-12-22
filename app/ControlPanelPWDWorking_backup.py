import pygame
import time
import datetime
import keyboard
import pygame
from pygame.locals import *
import random
from OpenGL.GL import *
from OpenGL.GLU import *
pygame.init()
screen = pygame.display.set_mode((1024, 600))

imageDirectory = "/Users/atulphadke/Documents/Energy/images/"
fontDirectory  = "/Users/atulphadke/Documents/Energy/fonts/"

finished = False
#resistance = 0

class ControlPanel_main:    
    imageDirectory = "/Users/atulphadke/Documents/Energy/images/"
    fontDirectory  = "/Users/atulphadke/Documents/Energy/fonts/"
    def __init__(self, previousImage, newImage):
        self.previousRes   = 0
        self.newRes        = 0
        self.previousImage = ControlPanel_main.imageDirectory + "beginning.png"
        self.newImage      = ControlPanel_main.imageDirectory + "beginning.png"
        
    def PulseWidthModulationBar(self):
        x, y = pygame.mouse.get_pos()
        yminvalue  = 475
        ymaxvalue  = 560
        image      = self.previousImage
        tmpImage   = ""
        resistance = -1
        if event.type == pygame.MOUSEBUTTONDOWN:
            if y >= 475 and y <= 560:
                if x >= 33 - 12.4 and x <= 33:
                        tmpImage = "beginning.png"
                        resistance = 0
                elif x >= 33 and x <= 33 + 12.4:
                        resistance = 1
                elif x >= 33 + 12.4 and x <= 33 + 24.8:
                        resistance = 2
                elif x >= 33 + 24.8 and x <= 33 + 37.2:
                        resistance = 3
                elif x >= 33 + 37.2 and x <= 33 + 49.6:
                        resistance = 4
                elif x >= 33 + 49.6 and x <= 33 + 62:
                        resistance = 5
                elif x >= 33 + (12.4)*5 and x <= 33 + (12.4)*6:
                        resistance = 6
                elif x >= 33 + (12.4)*6 and x <= 33 + (12.4)*7:
                        resistance = 7
                elif x >= 33 + (12.4)*7 and x <= 33 + (12.4)*8:
                        resistance = 8
                elif x >= 33 + (12.4)*8 and x <= 33 + (12.4)*9:
                        resistance = 9
                elif x >= 33 + (12.4)*9 and x <= 33 + (12.4)*10:
                        resistance = 10
                elif x >= 33 + (12.4)*10 and x <= 33 + (12.4)*11:
                        resistance = 11
                elif x >= 33 + (12.4)*11 and x <= 33 + (12.4)*12:
                        resistance = 12
                elif x >= 33 + (12.4)*12 and x <= 33 + (12.4)*13:
                        resistance = 13
                elif x >= 33 + (12.4)*13 and x <= 33 + (12.4)*14:
                        resistance = 14
                elif x >= 33 + (12.4)*14 and x <= 33 + (12.4)*15:
                        resistance = 15
                elif x >= 33 + (12.4)*15 and x <= 33 + (12.4)*16:
                        resistance = 16
                elif x >= 33 + (12.4)*16 and x <= 33 + (12.4)*17:
                        resistance = 17
                elif x >= 33 + (12.4)*17 and x <= 33 + (12.4)*18:
                        resistance = 18
                elif x >= 33 + (12.4)*18 and x <= 33 + (12.4)*19:
                        resistance = 19
                elif x >= 33 + (12.4)*19 and x <= 33 + (12.4)*20:
                        resistance = 20
                elif x >= 33 + (12.4)*20 and x <= 33 + (12.4)*21:
                        resistance = 21
                elif x >= 33 + (12.4)*21 and x <= 33 + (12.4)*22:
                        resistance = 22
                elif x >= 33 + (12.4)*22 and x <= 33 + (12.4)*23:
                        resistance = 23
                elif x >= 33 + (12.4)*23 and x <= 33 + (12.4)*24:
                        resistance = 24
                elif x >= 33 + (12.4)*24 and x <= 33 + (12.4)*25:
                        resistance = 25
                elif x >= 33 + (12.4)*25 and x <= 33 + (12.4)*26:
                        resistance = 26
                elif x >= 33 + (12.4)*26 and x <= 33 + (12.4)*27:
                        resistance = 27
                elif x >= 33 + (12.4)*27 and x <= 33 + (12.4)*28:
                        resistance = 28
                elif x >= 33 + (12.4)*28 and x <= 33 + (12.4)*29:
                        resistance = 29
                elif x >= 33 + (12.4)*29 and x <= 33 + (12.4)*30:
                        resistance = 30
        if resistance == -1:
            image = self.previousImage
            resistance = self.previousRes
        elif resistance == 0:
            image = imageDirectory + tmpImage        
        else:
            imageNum = resistance - 1
            if imageNum < 10:
                imageNum = "0" + str(imageNum)
            image = imageDirectory + "frame_" + str(imageNum) + "_delay-0.33s.png"
            resistance = resistance * 3.33
        #print(image)
        loadingicon = pygame.image.load(image)
        loadingicon = pygame.transform.scale(loadingicon, (400, 400))
        screen.blit(loadingicon, (20, 350))
        return image, resistance
    def Arrowbuttontext(self):
            NextPage = pygame.font.Font(fontDirectory + 'NanumGothic-Regular.ttf', 20)
            PageTurn = NextPage.render("Main Page", 20, (255, 255, 255))
            screen.blit(PageTurn, (650, 37))
    def Arrowbutton(self):
            arrow = pygame.image.load(imageDirectory + "ArrowNotHover.png")
            screen.blit(arrow, (200, -300))
            x, y = pygame.mouse.get_pos()
            if x >= 775 and x <= 980 and y >= 15 and y <= 85:
                    arrow = pygame.image.load(imageDirectory + "ArrowHover.png")
                    screen.blit(arrow, (200, -300))
                    if event.type == pygame.MOUSEBUTTONDOWN:
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
                                    if v == 1500:
                                        v = 0
                                        screen = pygame.display.set_mode((1024, 600))
                                        fin = False
                                        
                            main()
                            #fin = main()
                            #return fin
                                
    def ControlPanel(self):
            screen.fill((0,0,0))
            filename = fontDirectory + 'NanumGothic-Regular.ttf'
            Title = pygame.font.Font(filename, 50)
            title = Title.render("Control Panel", 100, (255, 255, 255))
            fontRes = pygame.font.Font(filename, 25)
            fontTrueEnergyOutput = pygame.font.Font(filename, 25)
            screen.blit(title, (20, 20))
            self.Arrowbutton()
            fin = self.Arrowbutton()
            self.Arrowbuttontext()
            #if fin == False:
                #quit()
            newImage, newRes = self.PulseWidthModulationBar()
            #print(newRes)
            previousImage = self.previousImage
            loadingicon = pygame.image.load(newImage)
            if newRes == previousRes:
                    resistance1 = fontRes.render(str(round(newRes)) + " Resistance", 100, (255, 255, 255))
                    TrueEnergyOutput = fontTrueEnergyOutput.render(str(100 - (round(newRes))) + \
                          " Energy Output", 100, (255, 255, 255))
            else:
                    resistance1 = fontRes.render(str(round(previousRes)) + " Resistance", 100, (255, 255, 255))
                    TrueEnergyOutput = fontTrueEnergyOutput.render(str(100 - (round(previousRes))) + \
                          " Energy Output", 100, (255, 255, 255))

            if newImage == previousImage:
                    loadingicon = pygame.image.load(newImage)
            else:
                    loadingicon = pygame.image.load(previousImage)

            loadingicon = pygame.transform.scale(loadingicon, (400, 400))
            screen.blit(loadingicon, (20, 350))
            screen.blit(resistance1, (450, 475))
            screen.blit(TrueEnergyOutput, (450, 550))
            return newRes, newImage

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
        if firstTime == 0:
            newRes, newImage = controlPanel_new.ControlPanel()
            firstTime = firstTime + 1
            if previousRes != newRes:
                previousRes = newRes
                previousImage = newImage
        if event.type == pygame.MOUSEBUTTONDOWN:
            newRes, newImage = controlPanel_new.ControlPanel()
            if previousRes != newRes:
                previousRes = newRes
                previousImage = newImage
        
        pygame.display.flip()
        
