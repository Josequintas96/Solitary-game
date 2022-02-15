import pygame
from pygame.locals import *
import sys
# from .2048_SS.logicT import *
# complete path => /Users/failop/Projects/p2048/2048_SS
#complete path => 2048_SS
sys.path.append('../')


pygame.init()


#title
pygame.display.set_caption("Solitary")
iconS = pygame.image.load("image/card_game.webp")
pygame.display.set_icon(iconS)

#size of the window
screen = pygame.display.set_mode((800,800)) #height X:800  weight Y: 600
                    #start at left up corner

#image:
A_Clover = pygame.image.load("image/Card/Clover/A_Clover.png")
A_Clover_retouch =  pygame.image.load("resized_image.png")



text = ""

offset_m = [0,0]


def Original(pX, pY):
    screen.blit(A_Clover,(pX, pY))
    
def Resize( pX,pY):
    screen.blit(A_Clover_retouch,(pX, pY))


running = True

while running:
    
    mx, my = pygame.mouse.get_pos()
    rot = 0
    loc = [mx , my]
    
    #screen.blit(pygame.transform.rotate(img,rot),(loc[0]+offset_m[0], loc[1]+offset[1]))
    
    
    # print("Super Array => ", gameX.array_illustration())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

    
    screen.fill((155 , 155, 155))
    #if bellow screen.fill, then the image will be bellow the color
    Original(-10,10)
    Resize(520,50)

    pygame.display.update()

