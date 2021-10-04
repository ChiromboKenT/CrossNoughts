import os
import pygame
from pygame.constants import QUIT


#Force Centering the Window
os.environ['SDL_VIDEO_CENTERED'] = '1'
#Initialise Pygame
pygame.init()
mainWindow = pygame.display.set_mode((800,600))

#Load Assets 
bg_desert = pygame.image.load("Backgrounds/desert.jpg","Bg-desert")

clock = pygame.time.Clock()

def re_Render():
    mainWindow.blit(bg_desert, (0,0))
    pygame.display.update()

class GameState():
    def __init__(self):
        pass 

class GameBoard():
    def __init__(self):
        pass


#Initialise game state
gameRunning = True
while gameRunning:
    clock.tick(30)
    #Create Event
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            gameRunning = False
    
    mainWindow.fill((0,0,0))
    #Display Update
    re_Render()
    pygame.display.update()

pygame.quit()