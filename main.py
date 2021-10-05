import os
import numpy as np
import pygame
from pygame.constants import QUIT


#Force Centering the Window
os.environ['SDL_VIDEO_CENTERED'] = '1'
#Initialise Pygame
pygame.init()
pygame.display.set_caption("Cross O's")
mainWindow = pygame.display.set_mode((800,600))
xOffset = 100;
yOffset = 80;

playerCross = -1
playerCircle = 1

#Load Assets 
bg_desert = pygame.image.load("Backgrounds/desert.jpg","Bg-desert")
cursor_img = pygame.image.load("Cursors/desertCursor2.png", "DesertCursor")
Circle_img = pygame.image.load("Sprites/O.png", "O")
Cross_img = pygame.image.load("Sprites/X.png", "X")

clock = pygame.time.Clock()

class GameState():
    def __init__(self,currentPlayer):
        self.player = currentPlayer
        self.gameResult = 0
        self.GameBoard = Board()
    
    def isWinningMove(self):
        board = self.GameBoard.board
        for row_sum in np.nditer(np.sum(board,1)):
            if(row_sum == 3 or row_sum == -3):
                gameResult = self.player
                return True
        for col_sum in np.nditer(np.sum(board,0)):
            if(col_sum == 3 or col_sum == -3):
                gameResult = self.player
                return True
        if(np.diagonal(board).sum() == 3 or np.diagonal(board).sum() == -3  
            or np.flipud(board).diagonal().sum() == -3 or np.flipud(board).diagonal().sum() == 3):
            gameResult = self.player
            return True
        return False




    

class Board():
    def __init__(self, rows,columns):
        self.board = np.zeros((rows,columns))

    def playerToken(self,row,col,player):
        self.board[row][col] = player

    def isValidPosition(self, row,col):
        return self.board[row][col] == 0

    def isBoardFull(self):
        for pos in np.nditer(self.board):
            if pos == 0:
                return False
        return True
    def winningMove(self, currentPlayer):
        for row in range(self.board.shape[0]):
            if self.board[row][0] == currentPlayer and self.board[row][1] == currentPlayer and self.board[row][2] == currentPlayer:
                pass

    def printBoard(self):
        print(self.board)
    


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



class GameBoard():
    def __init__(self,currentPlayer):
        self.player = currentPlayer


#Initialise game state
gameRunning = True
pygame.mouse.set_visible(False)
desertBoard = Board(3,3)
desertBoard.playerToken(1,2,playerCircle)
desertBoard.printBoard()
PlayerTurn = 1
CurrentPlayer = 0
while gameRunning:
    CurrentPlayer = PlayerTurn

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
    PlayerTurn *= -1

pygame.quit()