import pygame
from pygame.locals import *
import sys
import os.path
# from .2048_SS.logicT import *
# complete path => /Users/failop/Projects/p2048/2048_SS
#complete path => 2048_SS
sys.path.append('../')


pygame.init()


#title
pygame.display.set_caption("Libriary")
location_cecilia = "/Users/failop/Documents/Failop/Wostu/doc/Cecilia/"
arrow_l  = "arrow_left64.png"
arrow_left = pygame.image.load(arrow_l)
imageZ = "broken_image.png"

# iconS = pygame.image.load("image/card_game.webp")
# pygame.display.set_icon(iconS)

#size of the window
screen = pygame.display.set_mode((1200,840)) #height X:800  weight Y: 600
                    #start at left up corner

#iimage inserrt
image_c = None
pota = (650, 800)



def imageX(basic , tor, chapter, page):
    locX = basic + tor + str(chapter) + "_"+ str(page) +".png"
    # global image_c 
    # print(locX)
    image_c = None
    if not os.path.isfile(locX):
        locX = basic + tor + str(chapter) + "_"+ str(page) +".jpg"
        if not os.path.isfile(locX):
            image_c = pygame.image.load(imageZ)
            print("\tThere is an error:  ", locX)
        else:
            image_c = pygame.image.load(locX)
            image_c = pygame.transform.scale(image_c, pota)
            print("Size of image = ", image_c.get_size())
            # image_c = pygame.transform.scale(image_c, (800, 750))

    else:
        image_c = pygame.image.load(locX)
        image_c = pygame.transform.scale(image_c, pota)
        print("Size of image = ", image_c.get_size())
    return image_c

def display_image( px , py):
    screen.blit(imageX(location_cecilia, "c", chaptX , pageX), (px,py) )

def arr_left(px,py):
    screen.blit(arrow_left, (px,py) )
    
def rotate_arrow(angle, px, py):
    rotated_image = pygame.transform.rotate(arrow_left, angle)
    # new_rect = rotated_image.get_rect(center = arrow_left.get_rect(topleft = topleft).center)
    screen.blit(rotated_image, (px,py))
    
def control_image(loc):
    if loc[0] >90 and loc[0]<700:
        print("Connect image")
        return True
        # move_image(loc)
    return False

def move_image(loc):
    px2 = loc[0]
    px2 = 90
    if px2 < 90:
        px2 = 90
    
    py2 = 10-loc[1]
    display_image(px2,py2) 

def control_page(loc, control):
    global pageX
    global chaptX
    global px, py
    px = 90
    py = 10
    if control == "None": 
        print("Chapter: " , chaptX , "  ==> Prev: ", pageX)
        if loc[0] > 10 and loc[0] < 74:
            if loc[1] > 10 and loc[1] < 74:
                pageX -=1
                if pageX < 1:
                    pageX = 13
                    chaptX -=1
            elif loc[1] > 74 and loc[1] < 134:
                pageX +=1
                if pageX > 13:
                    pageX = 1
                    chaptX +=1
        print("Chapter: " , chaptX , "  ==> Prev: ", pageX)
    elif control == "Left": 
        pageX -=1
        if pageX < 1:
            pageX = 13
            chaptX -=1
    elif control == "Right": 
        pageX +=1
        if pageX > 13:
            pageX = 1
            chaptX +=1

px = 90
py = 10
scroll = False

chaptX = 4
pageX = 4

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
                control_page(loc, "None")
                if control_image(loc):
                    scroll = True
                
            # if event.button == 3:
            #     print("I don't know => Right click")
            # if event.button == 4:
            #     print("I don't know => midddle click")
            # if event.button == 5:
            #     print("I don't know => not middle click")
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                print("Button rise")
                scroll = False
                
        #if keystroke press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left arrrow press")
                # py  -=10
                control_page(loc, "Left")
            if event.key == pygame.K_RIGHT:
                print("Right key is press")
                # py += 10 
                control_page(loc, "Right")
            if event.key == pygame.K_0:
                print("Key is 0")
            elif event.key == pygame.K_1:
                print("Key is 1")
            elif event.key == pygame.K_2:
                print("Key is 2")
            elif event.key == pygame.K_3:
                print("Key is 3")
            elif event.key == pygame.K_4:
                print("Key is 4")
            elif event.key == pygame.K_5:
                print("Key is 5")
            elif event.key == pygame.K_6:
                print("Key is 6")
            elif event.key == pygame.K_7:
                print("Key is 7")
            elif event.key == pygame.K_8:
                print("Key is 8")
            elif event.key == pygame.K_9:
                print("Key is 9")

            if event.key == pygame.K_UP:
                print("Up key is press")
                px -=10

            if event.key == pygame.K_DOWN:
                print("Down key is press")
                px += 10
            
    
    screen.fill((155 , 155, 155))
    #if bellow screen.fill, then the image will be bellow the color

    if scroll:
        move_image(loc)
    else:
        display_image(px,py)
    arr_left(10,10)
    # arrow_l.scroll(10,10)

    rotate_arrow(180, 10, 70)

    pygame.display.update()

