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

#letters
letter_a = pygame.image.load("image/letter/a.png")
letter_b = pygame.image.load("image/letter/b.png")
letter_c = pygame.image.load("image/letter/c.png")
letter_d = pygame.image.load("image/letter/d.png")
letter_e = pygame.image.load("image/letter/e.png")
letter_f = pygame.image.load("image/letter/f.png")
letter_g = pygame.image.load("image/letter/g.png")
letter_h = pygame.image.load("image/letter/h.png")
letter_i = pygame.image.load("image/letter/i.png")
letter_j = pygame.image.load("image/letter/j.png")
letter_k = pygame.image.load("image/letter/k.png")
letter_l = pygame.image.load("image/letter/l.png")
letter_m = pygame.image.load("image/letter/m.png")
letter_n = pygame.image.load("image/letter/n.png")
letter_o = pygame.image.load("image/letter/o.png")
letter_p = pygame.image.load("image/letter/p.png")
letter_q = pygame.image.load("image/letter/q.png")
letter_r = pygame.image.load("image/letter/r.png")
letter_s = pygame.image.load("image/letter/s.png")
letter_t = pygame.image.load("image/letter/t.png")
letter_u = pygame.image.load("image/letter/u.png")

# letter_v = pygame.image.load("image/letter/f.png")
# letter_w = pygame.image.load("image/letter/g.png")
# letter_x = pygame.image.load("image/letter/h.png")
# letter_y = pygame.image.load("image/letter/i.png")
# letter_z = pygame.image.load("image/letter/j.png")


#numbI_one = pygame.image.load("numbers/numb/one_32.png")
board = pygame.image.load("image/board_512.png")

card_back = pygame.image.load("image/card_back.png")


teext = ""

offset_m = [0,0]




def Textmachine():
    # print("H")
    pictureTextMachine('a', 348, 348)
    
def pictureTextMachine(letterX,pX,pY):
    if letterX == 'a':
        Pletter_a(pX,pY)
        
    if letterX == 'b':
        Pletter_a(pX,pY)
    if letterX == 'c':
        Pletter_a(pX,pY)
    if letterX == 'd':
        Pletter_a(pX,pY)
    if letterX == 'e':
        Pletter_a(pX,pY)
    if letterX == 'f':
        Pletter_a(pX,pY)
    if letterX == 'g':
        Pletter_a(pX,pY)
    if letterX == 'h':
        Pletter_a(pX,pY)
    if letterX == 'i':
        Pletter_a(pX,pY)
    if letterX == 'j':
        Pletter_a(pX,pY)
    if letterX == 'k':
        Pletter_a(pX,pY)     
    if letterX == 'l':
        Pletter_a(pX,pY)
    if letterX == 'm':
        Pletter_a(pX,pY)
    if letterX == 'n':
        Pletter_a(pX,pY)
    if letterX == 'o':
        Pletter_a(pX,pY)
    if letterX == 'p':
        Pletter_a(pX,pY)   

def card_b(pX, pY):
    screen.blit(card_back,(pX, pY))
    
def card_b2( pX,pY):
    global card_back
    card_back = pygame.transform.scale(card_back, (pX, pY))


def board_b(pX, pY):
    screen.blit(board,(pX, pY))


def Pletter_a(pX, pY):
    screen.blit(letter_a,(pX, pY))
def Pletter_b(pX, pY):
    screen.blit(letter_b,(pX, pY))
def Pletter_c(pX, pY):
    screen.blit(letter_c,(pX, pY))
def Pletter_d(pX, pY):
    screen.blit(letter_d,(pX, pY))
def Pletter_e(pX, pY):
    screen.blit(letter_e,(pX, pY))
def Pletter_f(pX, pY):
    screen.blit(letter_f,(pX, pY))
def Pletter_g(pX, pY):
    screen.blit(letter_g,(pX, pY))
def Pletter_h(pX, pY):
    screen.blit(letter_h ,(pX, pY))
def Pletter_i(pX, pY):
    screen.blit(letter_i ,(pX, pY))
def Pletter_j(pX, pY):
    screen.blit(letter_j ,(pX, pY))
def Pletter_k(pX, pY):
    screen.blit(letter_k ,(pX, pY))
def Pletter_l(pX, pY):
    screen.blit(letter_l,(pX, pY))
def Pletter_m(pX, pY):
    screen.blit(letter_m,(pX, pY))
def Pletter_n(pX, pY):
    screen.blit(letter_n ,(pX, pY))
def Pletter_o(pX, pY):
    screen.blit(letter_o ,(pX, pY))
def Pletter_p(pX, pY):
    screen.blit(letter_p ,(pX, pY))
def Pletter_q(pX, pY):
    screen.blit(letter_q,(pX, pY))   
def Pletter_r(pX, pY):
    screen.blit(letter_r,(pX, pY))
def Pletter_s(pX, pY):
    screen.blit(letter_s,(pX, pY))
def Pletter_t(pX, pY):
    screen.blit(letter_t,(pX, pY))
def Pletter_u(pX, pY):
    screen.blit(letter_u,(pX, pY))






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
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("location is ", loc)
            if event.button == 3:
                print("I don't know => Right click")
            if event.button == 4:
                print("I don't know => midddle click")
            if event.button == 5:
                print("I don't know => not middle click")
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                print("Button rise")
            

        #if keystroke press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left arrrow press")
                
            if event.key == pygame.K_RIGHT:
                print("Right key is press")

            if event.key == pygame.K_UP:
                print("Up key is press")

            if event.key == pygame.K_DOWN:
                print("Down key is press")
                
            if event.key == pygame.K_SPACE:
                print("Space key button")
                
            if event.key == pygame.K_DELETE:
                print("Delete key button")

            if event.key == pygame.K_RETURN:
                print("Enter buttoon is pressed")
                card_b2(64,72)
            
            if event.key == pygame.K_a:
                print("Key a has been pressed")
            
            if event.key == pygame.K_b:
                print("Key b has been pressed")
                
            if event.key == pygame.K_c:
                print("Key c has been pressed")
                
            if event.key == pygame.K_d:
                print("Key d has been pressed")
                
            if event.key == pygame.K_e:
                print("Key e has been pressed")
                
            if event.key == pygame.K_f:
                print("Key f has been pressed")
                
            if event.key == pygame.K_g:
                print("Key g has been pressed")

            if event.key == pygame.K_h:
                print("Key h has been pressed")
                
            if event.key == pygame.K_i:
                print("Key i has been pressed")
                
            if event.key == pygame.K_j:
                print("Key j has been pressed")
                
            if event.key == pygame.K_k:
                print("Key k has been pressed")
                
            if event.key == pygame.K_l:
                print("Key l has been pressed")
                
            if event.key == pygame.K_m:
                print("Key m has been pressed")
                
            if event.key == pygame.K_n:
                print("Key n has been pressed")
                
            if event.key == pygame.K_o:
                print("Key o has been pressed")
                
            if event.key == pygame.K_p:
                print("Key p has been pressed")
                
            if event.key == pygame.K_q:
                print("Key q has been pressed")
                
            if event.key == pygame.K_r:
                print("Key r has been pressed")
                
            if event.key == pygame.K_s:
                print("Key s has been pressed")
                
            if event.key == pygame.K_t:
                print("Key t has been pressed")
                
            if event.key == pygame.K_u:
                print("Key u has been pressed")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                print("Left arrrow release")

            if event.key == pygame.K_RIGHT:
                print("Right arrrow release")

            if event.key == pygame.K_UP:
                print("Up arrrow release")

            if event.key == pygame.K_DOWN:
                print("Down arrow release")
            if event.key == pygame.K_DELETE:
                print("Delete key")

    
    
    screen.fill((155 , 155, 155))
    #if bellow screen.fill, then the image will be bellow the color
    card_b(10,10)
    board_b(288,288)
    Textmachine()

    pygame.display.update()

