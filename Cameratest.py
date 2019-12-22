import sys
import pygame
from pygame import camera

pygame.init()
pygame.camera.init()

#create fullscreen display 640x480
screen = pygame.display.set_mode((640,480),0)

#find, open and start low-res camera
cam_list = pygame.camera.list_cameras()
webcam = pygame.camera.Camera("192.168.1.24:8081",(32,24))
webcam.start()

while True:
    #grab image, scale and blit to screen
    imagen = webcam.get_image()
    imagen = pygame.transform.scale(imagen,(640,480))
    screen.blit(imagen,(0,0))

    #draw all updates to display
    pygame.display.update()

    # check for quit events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            webcam.stop()
            pygame.quit()
            sys.exit()
