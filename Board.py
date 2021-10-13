from typing import Text
from numpy.core.fromnumeric import compress
import pygame,sys
import console
from pygame.constants import K_RETURN, WINDOWENTER, K_r
from pygame.display import flip, update
from pygame.version import SDL

pygame.init()

board_color = (28,170,156)
line_color = (19,76,78) 
width = 15
player = 1


screen = pygame.display.set_mode((600,600))
screen.fill(board_color)
pygame.display.set_caption("Tic Tac Toe")

def draw_line():
    #horizontal line1
    pygame.draw.line(screen, line_color, (0,200), (600,200), width)
    #horizontal line2
    pygame.draw.line(screen, line_color, (0,400), (600,400), width)

    #vertical line1
    pygame.draw.line(screen,line_color,(200,0),(200,600),width )

    #vertical line2
    pygame.draw.line(screen,line_color,(400,0),(400,600),width )

draw_line()
pygame.display.update()

color = ()

def draw_vertical(col,player):
    posX = col*200+100

    if player == 1:
        color = (255,255,255)
    else:
        color = (65,65,65)

    pygame.draw.line(screen, color, (posX,15),(posX,600-15), width=15)
    pygame.display.flip()

def draw_horizontal(row,player):
    posY = row*200+100

    if player == 1:
        color = (255,255,255)
    else:
        color = (65,65,65)
    
    pygame.draw.line(screen, color, (15, posY), (600-15,posY), width=15)
    pygame.display.flip()

def draw_asc(player):
    if player == 1:
        color = (255,255,255)
    else:
        color = (65,65,65)

    pygame.draw.line(screen, color, (15, 600-15), (600-15,15), width=15)
    pygame.display.flip()

def draw_dec(player):
    if player == 1:
        color = (255,255,255)
    else:
        color = (65,65,65)

    pygame.draw.line(screen, color, (15,15), (600-15,600-15), width=15)
    pygame.display.flip()






def check_win(player):
    for col in range(3):
        if console.board[0][col] == player and console.board[1][col] == player and console.board[2][col] == player:
            draw_vertical(col,player)
            
            return True

    for row in range(3):
        if console.board[row][0] == player and console.board[row][1] == player and console.board[row][2] == player:
            draw_horizontal(row,player)        
            return True

    if  console.board[2][0] == player and console.board[1][1] == player and console.board[0][2] == player:
        draw_asc(player)
        return True


    if console.board[0][0] == player and console.board[1][1] == player and console.board[2][2] == player:
        draw_dec(player)
        return True

    return False


def draw_figure():
    for row in range(3):
        for col in range(3):
            if console.board[row][col] == 1:
                pygame.draw.circle(screen, (255,255,255), ((int(col*200 + 100)),(int(row*200 + 100))), 60 , 15)
                pygame.display.update()
                

            if console.board[row][col] == 2:
                pygame.draw.line(screen, (65,65,65), (col*200+55 ,row*200+200-55),(col*200+200-55,row*200+55), 15)
                pygame.draw.line(screen, (65,65,65), (col*200+55 ,row*200+55),(col*200+200-55,row*200+200-55), 15)
                pygame.display.update()






work = True
game_over = False
while work:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            click_col = mouseX//200
            click_row = mouseY//200

            if console.square_avail(click_row,click_col):

                if player == 1:
                    console.mark_square(click_row,click_col,player)
                    draw_figure()
                    if check_win(player):
                        game_over = True
                        break
                    player = 2
                    
                elif player == 2:
                    console.mark_square(click_row,click_col,player)
                    draw_figure()
                    if check_win(player):
                        game_over = True
                        break
                    player = 1

    if game_over:
        if player == 1:
            color = (255,255,255)
        else:
            color = (65,65,65)
        
        screen.fill(board_color)
        font = pygame.font.Font('/usr/share/fonts/truetype/msttcorefonts/Arial.ttf', 50)
        pygame.time.wait(450)
        winner = font.render(" Player "+str(player)+" won" ,True, color)
        screen.blit(winner,(100,100))
        pygame.display.flip()
