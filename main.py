import os
import math as mt
import numpy as np
import pygame
from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION, QUIT


#Force Centering the Window
os.environ['SDL_VIDEO_CENTERED'] = '1'
#Initialise Pygame
pygame.init()
pygame.display.set_caption("Ken's Cross O's")
mainWindow = pygame.display.set_mode((800,600))
xOffset = 100;
yOffset = 80;


GameLevel = 0
playerCross = -1
playerCircle = 1

#Load Assets 

cursor_img = pygame.image.load("Cursors/desertCursor2.png", "DesertCursor")
Circle_img = pygame.image.load("Sprites/O.png", "O")
Cross_img = pygame.image.load("Sprites/X.png", "X")

clock = pygame.time.Clock()

class GameState():
    gameResult = 0
    def __init__(self,currentPlayer,level):
        self.player = currentPlayer
        self.level = level
        self.GameBoard = Board(3,3,self.get_bg())
        

    def get_bg(self):
        if(self.level == 0):
            currentBg = pygame.image.load("Backgrounds/desert.jpg","Bg-desert")
        elif(self.level == 1):
            currentBg = pygame.image.load("Backgrounds/desert.jpg","Bg-desert")
        elif(self.level == 2):
            currentBg = pygame.image.load("Backgrounds/desert.jpg","Bg-desert")
        else:
            currentBg = pygame.image.load("Backgrounds/desert.jpg","Bg-desert")
        return currentBg
            

    def set_level(self, level):
        self.level = level
        self.GameBoard = Board(3,3,self.get_bg())
    
   

class Board():
    def __init__(self, rows,columns,boardImage):
        self.board = np.zeros((rows,columns))
        self.boardBackground = boardImage
        self.boardResult = 0

    def reset(self,rows,columns):
        self.board = np.zeros((rows,columns))
    def playerToken(self,row,col,player):
        if(self.isValidPosition(row,col)):
            self.board[row][col] = player
            if( self.isWinningMove(player)):
                self.GameOver(player)
                return False
        if(self.isBoardFull()):
            self.GameOver(2)
            return False
        return True

    def isValidPosition(self, row,col):
        return self.board[row][col] == 0

    def isBoardFull(self):
        for pos in np.nditer(self.board):
            if pos == 0:
                return False
        return True

    def isWinningMove(self,player):
        for row_sum in np.nditer(np.sum(self.board,1)):
            if(row_sum == 3 or row_sum == -3):
                self.boardResult = player
                return self.boardResult
        for col_sum in np.nditer(np.sum(self.board,0)):
            if(col_sum == 3 or col_sum == -3):
                self.boardResult = player
                return self.boardResult
        if(np.diagonal(self.board).sum() == 3 or np.diagonal(self.board).sum() == -3  
            or np.flipud(self.board).diagonal().sum() == -3 or np.flipud(self.board).diagonal().sum() == 3):
                self.boardResult = player
                return self.boardResult
        return 0
    
    def draw_rect_alpha(self,surface, color, pos,size):
        shape_surf = pygame.Surface(size, pygame.SRCALPHA)
        shape_surf.fill(color)
        surface.blit(shape_surf, pos)

    def renderBoard(self,Window):
        smallfont = pygame.font.SysFont('Corbel',35)
        Window.blit(self.boardBackground, (0,0))
        ##Draw Horizontal Lines
        pygame.draw.aaline(Window, (0,0,0), [xOffset,yOffset + 145], [800- xOffset,yOffset + 145], True)
        pygame.draw.aaline(Window, (0,0,0), [xOffset,yOffset + 293], [800- xOffset,yOffset + 293], True)
        ##Draw Vertical Lines
        pygame.draw.aaline(Window, (0,0,0), [xOffset + 200, yOffset], [xOffset + 200,600 - yOffset], True)
        pygame.draw.aaline(Window, (0,0,0), [xOffset + 400, yOffset], [xOffset + 400,600 - yOffset], True)

        #Draw Transparent Rectangle
        self.draw_rect_alpha(Window,(67,0,56,140), [xOffset,yOffset],(600,440))

        
        for cellIndex, cellValue in np.ndenumerate(self.board):
            if(cellValue == playerCross):
               Window.blit(Cross_img,((cellIndex[1] * 200) + xOffset + 24.5, (cellIndex[0] * 145) + yOffset))
            elif(cellValue == playerCircle):
                Window.blit(Circle_img,((cellIndex[1] * 200) + xOffset + 28.5, (cellIndex[0] * 145) + yOffset))

        
        if(GameState.gameResult != 0):
            text = smallfont.render('Play Again?' , True , (255,255,255))
            if(GameState.gameResult == playerCircle):
                winner = "Player 1 Won!"
            elif(GameState.gameResult == playerCross):
                winner = "Player 2 Won!"
            else:
                winner = "Draw!!"
            
            textWinner = smallfont.render(f"{winner}",True,(255,255,255))
            
            self.draw_rect_alpha(Window,(4,170,109,110), [0,0],(800,600))
            
            self.draw_rect_alpha(Window,(0,75,188,255), [xOffset + 100,yOffset + 100],(400,100))
            self.draw_rect_alpha(Window,(67,0,56,255), [xOffset + 200,yOffset + 300],(200,50))
            
            Window.blit(textWinner, [xOffset + 300 - textWinner.get_width()/2,yOffset + 150 - textWinner.get_height()/2])
            Window.blit(text, [xOffset + 300 - text.get_width()/2,yOffset + 325 - text.get_height()/2])

    def GameOver(self,result):
        GameState.gameResult = result
        print(f'Result : {result}')
        
        pygame.display.update()

def re_Render(Board):
    rectangleCoord = pygame.Rect(xOffset,yOffset,600,440)
    Board.renderBoard(mainWindow)
    cursor_img_rect = cursor_img.get_rect()
    
    
    ##DrawCursor
    cursor_img_rect.center = pygame.mouse.get_pos()  # update position 
    if(pygame.Rect.collidepoint(rectangleCoord, cursor_img_rect.center)):
        pygame.mouse.set_visible(False)
        mainWindow.blit(cursor_img, cursor_img_rect.center) # draw the cursor
    else:
        pygame.mouse.set_visible(True)

    pygame.display.update()



#Initialise game state
gameState = GameState(playerCross,GameLevel)
currentBoard = gameState.GameBoard
gameRunning = True

        

PlayerTurn = 1
CurrentPlayer = 0
clicked = False
nextTurn = 1
winButtonCoord =  pygame.Rect((xOffset + 178,yOffset + 278),(250,80))
#Game Loop
while gameRunning:
    CurrentPlayer = PlayerTurn

    clock.tick(30)
    #Create Event
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            gameRunning = False
        if event.type == MOUSEBUTTONDOWN:
            clicked = True
        if event.type == MOUSEBUTTONUP and clicked == True:
            
            if(pygame.Rect.collidepoint(winButtonCoord, event.pos) and GameState.gameResult != 0):
                currentBoard.reset(3,3)
                PlayerTurn = 1
                nextTurn = 1
                CurrentPlayer = 0
                GameState.gameResult = 0
            if(nextTurn):
                row = mt.floor((yOffset + event.pos[1])/146) - 1
                column = mt.floor((xOffset + event.pos[0])/200) -1
                nextTurn = currentBoard.playerToken(row,column,CurrentPlayer)
                PlayerTurn *= -1
            clicked = False
            
    mainWindow.fill((0,0,0))
    #Display Update
    re_Render(currentBoard)
    pygame.display.update()


    

pygame.quit()