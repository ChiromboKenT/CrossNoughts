import os
import pygame
from pygame.constants import QUIT
from pygame.display import set_caption


#Force Centering the Window
os.environ['SDL_VIDEO_CENTERED'] = '1'
#Initialise Pygame
pygame.init()
pygame.display.set_caption("Cross O's")
mainWindow = pygame.display.set_mode((800,600))
xOffset = 100;
yOffset = 80;

#Load Assets 
bg_desert = pygame.image.load("Backgrounds/desert.jpg","Bg-desert")
cursor_img = pygame.image.load("Cursors/desertCursor2.png", "DesertCursor")
Circle_img = pygame.image.load("Sprites/O.png", "O")
Cross_img = pygame.image.load("Sprites/X.png", "X")

clock = pygame.time.Clock()



def draw_rect_alpha(surface, color, pos):
    shape_surf = pygame.Surface((600,440), pygame.SRCALPHA)
    shape_surf.fill((67,0,56,140))
    surface.blit(shape_surf, pos)

def re_Render():
    mainWindow.blit(bg_desert, (0,0))
    cursor_img_rect = cursor_img.get_rect()

    draw_rect_alpha(mainWindow,(255,0,0), [xOffset,yOffset])
    ##Draw Horizontal Lines
    pygame.draw.aaline(mainWindow, (0,0,0), [xOffset,yOffset + 145], [800- xOffset,yOffset + 145], True)
    pygame.draw.aaline(mainWindow, (0,0,0), [xOffset,yOffset + 293], [800- xOffset,yOffset + 293], True)
    ##Draw Vertical Lines
    pygame.draw.aaline(mainWindow, (0,0,0), [xOffset + 200, yOffset], [xOffset + 200,600 - yOffset], True)
    pygame.draw.aaline(mainWindow, (0,0,0), [xOffset + 400, yOffset], [xOffset + 400,600 - yOffset], True)

    ##DrawCursor
    cursor_img_rect.center = pygame.mouse.get_pos()  # update position 
    mainWindow.blit(cursor_img, cursor_img_rect.center) # draw the cursor


    pygame.display.update()

class GameState():
    def __init__(self):
        pass 

class GameBoard():
    def __init__(self):
        pass


#Initialise game state
gameRunning = True
pygame.mouse.set_visible(False)
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