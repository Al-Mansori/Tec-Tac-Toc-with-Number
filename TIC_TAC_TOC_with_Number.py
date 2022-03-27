# TIC TAC TOC With Number_GUI 
# Made by Mohammed Saleh Al-Mansori 
# ID: 20210729
# 2022/3/3

import pygame
import sys
import numpy as np
pygame.init()
# constants
width = 600
height = width
line_width = 15
board_cols = 3
board_rows = 3
circle_radius = 60
circle_width = 15
cross_width = 25
space = 55
#colors
BG_color = (124,143,173)
line_black = (0,0,0)
red = (255,80,80)
blue = (80,80,255)
white = (255,255,255)
player_1 = (255,50,50)
player_2 = (50,50,255)


screen = pygame.display.set_mode((width,height))
# Hedar of the game
pygame.display.set_caption("TIC TAC TOC With Number")
screen.fill(BG_color)
# bord
board = np.zeros((board_rows,board_cols),dtype=int)

# draw the lins of the game like this shap "#"
def lines():
    screen.fill(BG_color)
    #1  uper horizontal
    pygame.draw.line(screen, line_black ,(0,200),(600,200),line_width)
    #2 lower horizontal
    pygame.draw.line(screen, line_black ,(0,400),(600,400),line_width)
    #1 first vertecal
    pygame.draw.line(screen, line_black ,(200,0),(200,600),line_width)
    #2 second vertecal
    pygame.draw.line(screen, line_black ,(400,0),(400,600),line_width)
    
# n here is the main input to choose a number to play  
global n
n = 1
# this function draw the input on pygame screen 
def draw_number():
    global n
    for row in range(board_rows):
        for col in range(board_cols):
                if board[row][col] != -50:
                    myFont = pygame.font.SysFont("Times New Roman", 75)
                    randNumLabel = myFont.render(str(board[row][col]), 1, line_black)
                    screen.blit(randNumLabel, (col * 200 + 75,row * 200 + 75))
                
# this function mark the square each square marke just one time if all square full or marked then the game is over 
def mark_square(row,col):
    global n
    board[row][col] = n


# here we chake if th square availabel or not 
def availabel_square(row,col):
    if board[row][col] == -50:
        return True
    else:
        return False


# chake if the game Draw or not 

def is_board_full():
    for row in range(board_rows):
        for col in range(board_cols):
            if (board[row][col]) ==-50:
                return False
    lines()
    myFont = pygame.font.SysFont("Times New Roman", 60)
    randNumLabel = myFont.render("Draw", 1, white)
    screen.blit(randNumLabel, (220,150))
    return True
    
       
# cheke winner when ny adding 3 squares if the total sum is 15 then we have winner
def check_win(player):
   # vertical win chack
    for col in range(board_cols):
        if board[0][col] + board[1][col] + board[2][col] == 15:
            lines()
            draw_vertical_winning_line(col,player)
            return True
    # horizontal win chack
    for row in range(board_rows):
        if board[row][0] + board[row][1] + board[row][2] == 15:
            lines()
            draw_horizontal_winning_line(row,player)
            return True
    # asc diagonal win chack like this line '\'
    if board[2][0] + board[1][1] + board[0][2] == 15:
        lines()
        draw_asc_diagonal(player)
        return True
    # decs diagonal win chack like this line '/'
    if board[0][0] + board[1][1] + board[2][2] == 15:
        lines()
        draw_desc_diagonal(player)
        return True
    return False
# after we cheke the winner function we have to draw a line on the squares that total sum is 15 
def draw_vertical_winning_line(col,player):
    posX = col * 200 + 100
    if player == 1:
        color = player_2
    elif player == 2:
        color = player_1
    pygame.draw.line(screen,color,(posX,15),(posX,height - 15),15)
def draw_horizontal_winning_line(row,player):
    posY = row * 200 + 100
    if player == 1:
        color = player_2
    elif player == 2:
        color = player_1
    pygame.draw.line(screen,color,(15,posY),(height - 15,posY),15)


def draw_asc_diagonal(player):
    if player == 1:
        color = player_2
    elif player == 2:
        color = player_1
    pygame.draw.line(screen,color,(15,height - 15),(width - 15,15),15)
def draw_desc_diagonal(player):
    if player == 1:
        color = player_2
    elif player == 2:
        color = player_1
    pygame.draw.line(screen,color,(15,15),(width - 15,height - 15),15)
# this function restart the game by prees 'r' if u whant to play anuther raund
def restart():
    screen.fill(BG_color)
    lines()
    myFont = pygame.font.SysFont("Times New Roman", 32)
    randNumLabel = myFont.render("choose from 0 to 9 only", 1, white)
    screen.blit(randNumLabel, (150,100))
    myFont = pygame.font.SysFont("Times New Roman", 32)
    randNumLabel = myFont.render("Don't Repeat a number twice", 1, white)
    screen.blit(randNumLabel, (130,150))
    myFont = pygame.font.SysFont("Times New Roman", 32)
    randNumLabel = myFont.render("Enter an odd number then click on square", 1, blue)
    screen.blit(randNumLabel, (50,220))
    for row in range(board_rows):
        for col in range(board_cols):
            board[row][col] = -50
    start()
# this function cheke if the number is alrady markd on any square or not 
def board_has_num(n):
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == n:
                return True
    return False
# main function
def start():
    
    game_over = False
    player = 1
    global n
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                
                
                lines()
                draw_number()
                mouseX = event.pos[0] # x
                mouseY = event.pos[1] # y
            
                clicked_row = int(mouseY // 200)
                clicked_col = int(mouseX // 200)

         

                if availabel_square(clicked_row,clicked_col) and not board_has_num(n) and n % 2 == player % 2:
                     if player == 1:
                         mark_square(clicked_row,clicked_col)
                         is_board_full()
                         if check_win(player):
                             game_over = True
                             myFont = pygame.font.SysFont("Times New Roman", 60)
                             randNumLabel = myFont.render("Press r to restart", 1, white)
                             screen.blit(randNumLabel, (110,200))
                             myFont = pygame.font.SysFont("Times New Roman", 60)
                             randNumLabel = myFont.render("Winner", 1, blue)
                             screen.blit(randNumLabel, (210,150))
                         else:
                             if is_board_full()==False:
                                player = 2
                                myFont = pygame.font.SysFont("Times New Roman", 32)
                                randNumLabel = myFont.render("Enter even number then click on square", 1, red)
                                screen.blit(randNumLabel, (55,40))
                     elif player == 2:
                         mark_square(clicked_row,clicked_col)
                         is_board_full()
                         if check_win(player):
                             
                             game_over = True
                             myFont = pygame.font.SysFont("Times New Roman", 60)
                             randNumLabel = myFont.render("Press r to restart", 1, white)
                             screen.blit(randNumLabel, (110, 200))
                             myFont = pygame.font.SysFont("Times New Roman", 60)
                             randNumLabel = myFont.render("Winner", 1, red)
                             screen.blit(randNumLabel, (210,150))
                         else:
                             if is_board_full()==False:
                                player = 1
                                myFont = pygame.font.SysFont("Times New Roman", 32)
                                randNumLabel = myFont.render("Enter odd number then click on square", 1, blue)
                                screen.blit(randNumLabel, (55,40))
                     draw_number()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart()
                if event.key == pygame.K_1:
                    n = 1
                if event.key == pygame.K_2:
                    n = 2
                if event.key == pygame.K_3:
                    n = 3
                if event.key == pygame.K_4:
                    n = 4
                if event.key == pygame.K_5:
                    n = 5
                if event.key == pygame.K_6:
                    n = 6
                if event.key == pygame.K_7:
                    n = 7
                if event.key == pygame.K_8:
                    n = 8
                if event.key == pygame.K_9:
                    n = 9
                if event.key == pygame.K_0:
                    n = 0


        pygame.display.update()

lines()
restart()
