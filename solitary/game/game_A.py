import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
from pygame.locals import *
from data.settings_game.download_control import *
# from settings_game.collection_object import *
# from settings_game.display_control import *
import sys


# sys.path.append('../')
# from solitary_logic import Solitary
from data.solitary_logic import Solitary

pygame.init()


#title
pygame.display.set_caption("Solitary")
iconS = pygame.image.load("image/card_game.webp")
pygame.display.set_icon(iconS)

#size of the window
screen = pygame.display.set_mode((900,800)) #height X:800  weight Y: 600
                    #start at left up corner


# how to set up a card from the deck on specific location
def card_set_up(game_Omega, pX,pY, id):
    card_O = game_Omega[0].obtaincard(id)
    # card_O.description()
    new_symbol = card_O.ret_type()
    new_number = card_O.ret_value()
    if card_O.ret_state == "hidden":
        card_b(px,py)
    elif new_symbol == "Clover":
        if new_number == "ACE":
            screen.blit(cA_Clover,(pX, pY))
        elif new_number == "TWO":
            screen.blit(c2_Clover,(pX, pY))
        elif new_number == "THREE":
            screen.blit(c3_Clover,(pX, pY))
        elif new_number == "FOUR":
            screen.blit(c4_Clover,(pX, pY))
        elif new_number == "FIVE":
            screen.blit(c5_Clover,(pX, pY))
        elif new_number == "SIX":
            screen.blit(c6_Clover,(pX, pY))
        elif new_number == "SEVEN":
            screen.blit(c7_Clover,(pX, pY))
        elif new_number == "EIGHT":
            screen.blit(c8_Clover,(pX, pY))
        elif new_number == "NINE":
            screen.blit(c9_Clover,(pX, pY))
        elif new_number == "TEN":
            screen.blit(c10_Clover,(pX, pY))
        elif new_number == "JACK":
            screen.blit(cJ_Clover,(pX, pY))
        elif new_number == "QUEEN":
            screen.blit(cQ_Clover,(pX, pY))
        elif new_number == "KING":
            screen.blit(cK_Clover,(pX, pY))
            
    elif new_symbol == "Heart":
        if new_number == "ACE":
            screen.blit(cA_Heart,(pX, pY))
        elif new_number == "TWO":
            screen.blit(c2_Heart,(pX, pY))
        elif new_number == "THREE":
            screen.blit(c3_Heart,(pX, pY))
        elif new_number == "FOUR":
            screen.blit(c4_Heart,(pX, pY))
        elif new_number == "FIVE":
            screen.blit(c5_Heart, (pX, pY))
        elif new_number == "SIX":
            screen.blit(c6_Heart,(pX, pY))
        elif new_number == "SEVEN":
            screen.blit(c7_Heart,(pX, pY))
        elif new_number == "EIGHT":
            screen.blit(c8_Heart,(pX, pY))
        elif new_number == "NINE":
            screen.blit(c9_Heart,(pX, pY))
        elif new_number == "TEN":
            screen.blit(c10_Heart, (pX, pY))
        elif new_number == "JACK":
            screen.blit(cJ_Heart,(pX, pY))
        elif new_number == "QUEEN":
            screen.blit(cQ_Heart,(pX, pY))
        elif new_number == "KING":
            screen.blit(cK_Heart,(pX, pY))
            
    elif new_symbol == "Spades":
        if new_number == "ACE":
            screen.blit(cA_Pica,(pX, pY))
        elif new_number == "TWO":
            screen.blit(c2_Pica,(pX, pY))
        elif new_number == "THREE":
            screen.blit(c3_Pica,(pX, pY))
        elif new_number == "FOUR":
            screen.blit(c4_Pica,(pX, pY))
        elif new_number == "FIVE":
            screen.blit(c5_Pica,(pX, pY))
        elif new_number == "SIX":
            screen.blit(c6_Pica,(pX, pY))
        elif new_number == "SEVEN":
            screen.blit(c7_Pica,(pX, pY))
        elif new_number == "EIGHT":
            screen.blit(c8_Pica,(pX, pY))
        elif new_number == "NINE":
            screen.blit(c9_Pica,(pX, pY))
        elif new_number == "TEN":
            screen.blit(c10_Pica,(pX, pY))
        elif new_number == "JACK":
            screen.blit(cJ_Pica,(pX, pY))
        elif new_number == "QUEEN":
            screen.blit(cQ_Pica,(pX, pY))
        elif new_number == "KING":
            screen.blit(cK_Pica,(pX, pY))
            
    elif new_symbol == "Diamond":
        if new_number == "ACE":
            screen.blit(cA_Diamond,(pX, pY))
        elif new_number == "TWO":
            screen.blit(c2_Diamond,(pX, pY))
        elif new_number == "THREE":
            screen.blit(c3_Diamond,(pX, pY))
        elif new_number == "FOUR":
            screen.blit(c4_Diamond, (pX, pY))
        elif new_number == "FIVE":
            screen.blit(c5_Diamond, (pX, pY))
        elif new_number == "SIX":
            screen.blit(c6_Diamond, (pX, pY))
        elif new_number == "SEVEN":
            screen.blit(c7_Diamond, (pX, pY))
        elif new_number == "EIGHT":
            screen.blit(c8_Diamond, (pX, pY))
        elif new_number == "NINE":
            screen.blit(c9_Diamond, (pX, pY))
        elif new_number == "TEN":
            screen.blit(c10_Diamond, (pX, pY))
        elif new_number == "JACK":
            screen.blit(cJ_Diamond, (pX, pY))
        elif new_number == "QUEEN":
            screen.blit(cQ_Diamond, (pX, pY))
        elif new_number == "KING":
            screen.blit(cK_Diamond, (pX, pY))
        
            
            
## SET UP GAME => set up game object here
gameX = Solitary()
# game_Omega = Solitary()
game_Omega = [gameX]
# game_Omega[0].superman
game_Omega[0].set_up_game()
# game_Omega[0].manual_set_up_game6()



#print("Card Back width: ", card_back.get_width() )
#print("Card Back height: ", card_back.get_height() )


text = ""

offset_m = [0,0]


def card_b(pX, pY):
    # design of the back card
    screen.blit(card_back,(pX, pY))
def card_Diamond(pX, pY):
    # design of the diamond card
    screen.blit(c_Diamond,(pX, pY))
def card_Heart(pX, pY):
    # design of the heart card
    screen.blit(c_Heart,(pX, pY))
def card_Pica(pX, pY):
    # design of the Pica card
    screen.blit(c_Pica,(pX, pY))
def card_Clover(pX, pY):
    # design of the Clover card
    screen.blit(c_Clover,(pX, pY))
def score_d(pX,pY,numb):
    if numb ==0:
        screen.blit(numb_0,(pX, pY))
    elif numb ==1:
        screen.blit(numb_1,(pX, pY))
    elif numb==2:
        screen.blit(numb_2,(pX, pY))
    elif numb ==3:
        screen.blit(numb_3,(pX, pY))
    elif numb==4:
        screen.blit(numb_4,(pX, pY))
    elif numb==5:
        screen.blit(numb_5,(pX, pY))
    elif numb==6:
        screen.blit(numb_6,(pX, pY))
    elif numb==7:
        screen.blit(numb_7,(pX, pY))
    elif numb==8:
        screen.blit(numb_8,(pX, pY))
    elif numb==9:
        screen.blit(numb_9,(pX, pY))
    
    
def set_numb(pX,pY,score):
    numb_l = str(score)
    lenX = len(numb_l)
    i0 = 0
    li2=0
    while lenX > i0 :
        li = int(numb_l[li2])
        score_d(pX-30*lenX-1,pY,li)
        lenX-=1
        li2+=1




# Print letter of thee game
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
    
def congratulationX(pX,pY):
    screen.blit(congratulation, (pX, pY))
def undo_button(pX, pY, loc):
    if loc[0] > 40 and loc[0]<104 and loc[1] > 702 and loc[1]<766:
            screen.blit(undo_s, (pX-8, pY-8))
    else:
        screen.blit(undo_b, (pX, pY))
def new_g__button(pX, pY, loc):
    if loc[0] > 792 and loc[0]<856 and loc[1] > 702 and loc[1]<766:
            screen.blit(new_game_s, (pX-8, pY-8))
    else:
        screen.blit(new_game, (pX, pY))
def cover_empty(pX,pY):
    screen.blit(card_empty ,(pX, pY))
def board_new(pX,pY):
    screen.blit(board_new_g ,(pX, pY))
def score_board(pX, pY):
    Pletter_s(pX, pY)
    Pletter_c(pX+30, pY)
    Pletter_o(pX+30*2, pY)
    Pletter_r(pX+30*3, pY)
    Pletter_e(pX+30*4, pY)
    

numb = 50 #value too separrate the spare decks

#object collectionfor each agrupation of card
class collection():
    relative_loc = [0,0]
    location = [0,0]
    name =""
    spare_number = -1
    quantity = 5
    
    def __init__(self, px, py):
        self.location=[px,py]
        self.relative_loc = [px,py]
        
    def set_spare(self, id):
        self.spare_number = id
    def set_quantity(self, new_qua):
        self.quantity = new_qua
        
    def return_quantity(self):
        return self.quantity
    
    def set_name(self, new_name):
        self.name = new_name
    def set_Quatity(self, i0):
        self.quantity = i0
        #print("\t New Quanttity is ",self.quantity)
            
            
    def display(self, game_Omega, dynamic, new_loc, hyper_dynamic, stage_s, i0, card_grabbed_id):
        # dynamic refer if one card is on hnad
        #hyoper refer wheen seeveral hands are on hold
        #stage_S refer to  loocalization 
        if hyper_dynamic == False and dynamic == False:
            self.display_static(game_Omega, self.quantity,i0)
        elif hyper_dynamic:
            #print("Hyper Dynamic")
            self.display_static(game_Omega, stage_s, i0)
            self.display_advance_dynamic(game_Omega , new_loc, stage_s, i0)
            # self.display_dynamic(game_Omega, new_loc)
        elif dynamic:
            # print("Dynamic")
            self.display_static(game_Omega, self.quantity-1,  i0)
            self.display_dynamic(game_Omega, new_loc, i0, card_grabbed_id)
            
    
    def ret_loc(self):
        return self.location
        
    def display_static(self, game_Omega, set_quantity, i02):
        # picture the the cards of list that stay in place 
        i0 = 0
        distance_c = 20 #distance between cards
        cover_empty(self.location[0], self.location[1]+distance_c*i0)
        while i0 < set_quantity:
            # if state == hidden
            # print("\ti0: ", i0, " and i02: ", i02)
            # print("\t\tLength of Probl. ", len(game_Omega[0].listSpare[i02]))
            #add special safe to verifhy it is working 
            lenX2 = len(game_Omega[0].listSpare[i02])
            if i0 < lenX2:
                numb_id = game_Omega[0].listSpare[i02][i0]
                
                card_O = game_Omega[0].obtaincard(numb_id)
                if card_O.ret_state() == "reveal":
                    card_set_up( game_Omega ,self.location[0], self.location[1]+distance_c*i0, numb_id)
                else:
                    card_b(self.location[0], self.location[1]+distance_c*i0)
            i0 += 1
        
        
    def display_dynamic(self, game_Omega, new_loc, i0, card_grabbed_id):
         # picture the the one card oof list that move with our hand 
        numb_id = game_Omega[0].listSpare[i0][len(game_Omega[0].listSpare[i0])-1]
        card_grabbed_id[0] = numb_id
        card_set_up( game_Omega , new_loc[0]-40, new_loc[1]-53, numb_id )
        # card_b(new_loc[0]-40, new_loc[1]-53)
        
    def display_advance_dynamic(self, game_Omega, new_loc, stage_s, spare_numb):
         # picture the X's cards of list that movee with our mouse
        # #print("\tself.quatity => ", self.quantity) 
        # #print("\tstagee_s => ", stage_s) 
        i0 = self.quantity - stage_s
        distance_c = 20 #distance between cards
        i02 = 0
        while i02 < i0:
            numb_id = game_Omega[0].listSpare[spare_numb][i02+stage_s]
            card_set_up(game_Omega, new_loc[0]-40, new_loc[1]-53+distance_c*i02,numb_id )
            i02+=1
    
        
        
    def display_special(self, game_Omega, conditionX, symbol_name, new_loc):
        # special method set up for each of one collleection 
        # which deal with collection of samesymbol card
        # conditionX mean thatwee are grabbing a crad, therefore, top card of deck is above
        # symbol_name mean the card using at moment
        if self.quantity == 0:
            if self.name == "Clover":
                card_Clover(self.location[0], self.location[1])
            elif self.name == "Heart":
                card_Heart(self.location[0], self.location[1])
            elif self.name == "Pica":
                card_Pica(self.location[0], self.location[1])
            elif self.name == "Diamond":
                card_Diamond(self.location[0], self.location[1])
        elif self.quantity >=0:
            if self.name == "Clover":
                if self.quantity -1 == 0:
                    card_Clover(self.location[0], self.location[1])
                    if conditionX == True and symbol_name == self.name:
                        card_set_up(game_Omega, new_loc[0]-40, new_loc[1]-53, 0)
                    else:
                        card_set_up(game_Omega, self.location[0], self.location[1], 0)
                else:
                    card_set_up(game_Omega, self.location[0], self.location[1], self.quantity-2)
                    if conditionX == True and symbol_name == self.name:
                        card_set_up(game_Omega, new_loc[0]-40, new_loc[1]-53, self.quantity-1)
                    else:
                        card_set_up(game_Omega, self.location[0], self.location[1], self.quantity-1)
                    # card_set_up(game_Omega, self.location[0], self.location[1], self.quantity-1)
            elif self.name == "Heart":
                if self.quantity -1 == 0:
                    card_Heart(self.location[0], self.location[1])
                    if conditionX == True and symbol_name == self.name:
                        card_set_up(game_Omega, new_loc[0]-40, new_loc[1]-53, 39)
                    else:
                        card_set_up(game_Omega, self.location[0], self.location[1], 39)
                else:
                    card_set_up(game_Omega, self.location[0], self.location[1], self.quantity-2+39)
                    if conditionX == True and symbol_name == self.name:
                        card_set_up(game_Omega, new_loc[0]-40, new_loc[1]-53, self.quantity-1+39)
                    else:
                        card_set_up(game_Omega, self.location[0], self.location[1], self.quantity-1+39)
                    # card_set_up(game_Omega, self.location[0], self.location[1], self.quantity-1+39)
            elif self.name == "Pica":
                # print("QUANTITY OF PICA: ", self.quantity)
                if self.quantity -1 == 0:
                    card_Pica(self.location[0], self.location[1])
                    if conditionX == True and symbol_name == self.name:
                        card_set_up(game_Omega, new_loc[0]-40, new_loc[1]-53, 26)
                    else:
                        card_set_up(game_Omega, self.location[0], self.location[1], 26)
                    # card_set_up(game_Omega, self.location[0], self.location[1], 26)
                else:
                    card_set_up(game_Omega, self.location[0], self.location[1], self.quantity-2+26)
                    if conditionX == True and symbol_name == self.name:
                        card_set_up(game_Omega, new_loc[0]-40, new_loc[1]-53, self.quantity-1+26)
                    else:
                        card_set_up(game_Omega, self.location[0], self.location[1], self.quantity-1+26)
                    # card_set_up(game_Omega, self.location[0], self.location[1], self.quantity-1+26)
            elif self.name == "Diamond":
                if self.quantity -1 == 0:
                    card_Diamond(self.location[0], self.location[1])
                    # card_set_up(game_Omega, self.location[0], self.location[1], 13)
                    if conditionX == True and symbol_name == self.name:
                        card_set_up(game_Omega, new_loc[0]-40, new_loc[1]-53, 13)
                    else:
                        card_set_up(game_Omega, self.location[0], self.location[1], 13)
                else:
                    card_set_up(game_Omega, self.location[0], self.location[1], self.quantity-2+13)
                    if conditionX == True and symbol_name == self.name:
                        card_set_up(game_Omega, new_loc[0]-40, new_loc[1]-53, self.quantity-1+13)
                    else:
                        card_set_up(game_Omega, self.location[0], self.location[1], self.quantity-1+13)
                    # card_set_up(game_Omega, self.location[0], self.location[1], self.quantity-1+13)
        
            
        
    def move_loc(self, new_loc):
        self.location = new_loc 
        
    def grab_control_d(self, px, py):
        # grab control deck mean that if you press the deck 
        # we could deal with display cards 
        i0 = 2
        distance_c = 20 #distance between cards
        ix = 120+i0*distance_c
        if px >= distance_c and px <= distance_c+80:
            if py >=10 and py<=10+105:
                #print("You have press the DECK")
                return True
        return  False


    
    def grab_control_m(self, px, py):
        # grab control maneable mean 
        # that you are dealing with the card tht can be move around
        i0 = 2
        distance_c = 20 #distance between cards
        ix = 120+i0*distance_c
        if px >= ix and px <= ix+80:
            if py >= 10 and py <= 10+105:
                #print("YOU HAVE GRAB CONTROL")
                return True
        return  False
    
    def grab_advance(self, game_Omega, px,py, spare_num ,list_k):
        #meethod on colleection to verify is advanse_mouse can bee apply
        #list_k: list where will be save the number of the list
        i0 = self.quantity-1
        distance_c = 20 #distance between cards
        if px >= self.location[0] and px <= self.location[0]+80:
            #grab any card aboove the last card
            if i0+1 > 1:
                while i0 > 0:
                    if py < self.location[1]+distance_c*i0 and py >= self.location[1]+distance_c*(i0-1):
                        # global game_Omega
                        if game_Omega[0].check_list_Unorganize(spare_num, i0-1):
                            ##print("Advance Grab card == spare_num: ", spare_num, "\t i0: ",i0-1)
                            list_k[0] = (i0-1)
                            return True
                        else:
                            ##print("You grab card, but it is not unoganize")
                            return False
                    i0-=1
        return False
        
    def grab_c(self,px,py):
        i0 = self.quantity-1
        distance_c = 20 #distance between cards
        # #print("Self quantity: ", i0+1)
        if px >= self.location[0] and px <= self.location[0]+80:
            #grab last card
            if py >= self.location[1]+distance_c*i0 and py <= self.location[1]+distance_c*i0+105:
                #print("Super Grab card")
                return True
        return False
    
    def place_c(self,px,py):
        i0 = self.quantity-1
        distance_c = 20 #distance between cards
        #print("Self quantity: ", i0+1)
        if px >= self.location[0] and px <= self.location[0]+80:
            #grab last card
            if py >= self.location[1]+distance_c*i0 and py <= self.location[1]+distance_c*i0+105:
                #print("Super Grab card")
                return True
        return False
    
    def grab_special(self,px,py):
        if px >= self.location[0] and px <= self.location[0]+80:
            #grab last card
            if py >= self.location[1] and py <= self.location[1]+105:
                #print("Super Grab card")
                return True
        return False
    


def Grab_column(loc , control_mouse):
    control_mouse[0] = 1
    return coll1.grab_c(loc[0],loc[1])


def grab_control_c(loc, cc, loc_collection):
    # grab control collection meean that if you press the collection 
    # so know we can grab deetermine card 
    py = loc[1]
    px = loc[0]
    ix = 90
    if py >=10 and py<=10+105:
        if px >= loc_collection[0] and px <= loc_collection[0]+80:
            cc[0] = "Pica"
            #print("You have press the collection of Pica => ", cc)
            return True
        elif px >= loc_collection[0]-ix and px <= loc_collection[0]-ix+80:
            cc[0] = "Heart"
            #print("You have press the collection of Heart")
            return True
        elif px >= loc_collection[0]-ix*2 and px <= loc_collection[0]-ix*2+80:
            cc[0] = "Diamond"
            #print("You have press the collection of Diamond")
            return True
        elif px >= loc_collection[0]-ix*3 and px <= loc_collection[0]-ix*3+80:
            cc[0] = "Clover"
            #print("You have press the collection of Clover")
            return True
    return  False


def display_spare_deck(game_Omega, collectionU, loc, control_mouse, advance_mouse, card_grabbed_id):
    i0 = 0
    while i0<7:
        if i0 == control_mouse[0]:
            i0 = i0
            #original version
            # if advance_mouse[0] != -1:
            #     #print("SUPER ADVANCE MOUSE BUTTON")
            #     collectionU[i0].display(game_Omega, True, loc, True, advance_mouse[0], i0, card_grabbed_id)
            # else:
            #     collectionU[i0].display(game_Omega, True, loc, False, -1, i0, card_grabbed_id)
        else:
            collectionU[i0].display(game_Omega , False, loc, False, -1,i0, card_grabbed_id)
        i0+=1
    #rearrengee to set up next run
    if control_mouse[0] < 7 and control_mouse[0] >= 0:
        i0 = control_mouse[0]
        if advance_mouse[0] != -1:
                #print("SUPER ADVANCE MOUSE BUTTON")
            collectionU[i0].display(game_Omega, True, loc, True, advance_mouse[0], i0, card_grabbed_id)
        else:
            collectionU[i0].display(game_Omega, True, loc, False, -1, i0, card_grabbed_id)

        
        
    
def display_collection(game_Omega, grab_happen, symbol_name, new_loc):
    coll_Pica.display_special(game_Omega,grab_happen, symbol_name ,new_loc)
    coll_Clover.display_special(game_Omega,grab_happen, symbol_name ,new_loc)
    coll_Diamond.display_special(game_Omega, grab_happen, symbol_name ,new_loc)
    coll_Heart.display_special(game_Omega, grab_happen, symbol_name ,new_loc)
    
    
def display_control_deck(game_Omega, loc, grab):
    display_control(game_Omega, loc, grab)
    
def display_control(game_Omega, new_loc, grab):
    i0 = len(game_Omega[0].listControl)-game_Omega[0].setcount[0]
    distance_c = 20  #distance between cards
    if i0 <= 0:
        cover_empty(distance_c, 10)
        # screen.blit(card_empty ,(distance_c, 10))
    else:
        card_b(distance_c,10)
    listK = game_Omega[0].set_card()
    i02 = len(listK)
    i03 = 0
    if grab == True:
        i02 = i02-1
    while i03< i02:
        card_set_up(game_Omega, 120+i03*distance_c,10, listK[i03])
        i03+=1
    if grab == True:
        card_set_up(game_Omega, new_loc[0]-40, new_loc[1]-53+distance_c*i02, listK[len(listK)-1])

def grab_control_deck(self, game_Omega):
    if coll_Control.grab_control_d(loc[0], loc[1]):
        # print("\t GRAB DEECK ==> THEREFORE EXPAND CARDS")
        game_Omega[0].set_control()
        game_Omega[0].record_set()
        #print("\t\t this is the new control count ",  game_Omega[0].setcount)
    elif coll_Control.grab_control_m(loc[0], loc[1]):
        # print("\t GRAB EXTRA DECK ==> THEREFORE manage CARDS")
        return True
    return False

def grab_spare_deck(game_Omega, collectionU, loc, control_mouse, advance_mouse):
    i0 = 0
    while i0 < 7:
        list_k= [-1]
        # global control_mouse
        if collectionU[i0].grab_advance(game_Omega, loc[0], loc[1], i0 ,list_k):
            control_mouse[0] = i0
            advance_mouse[0] = list_k[0]
            list_k.clear()
            
            numb_id = game_Omega[0].listSpare[control_mouse[0]][advance_mouse[0]]
            card_O = game_Omega[0].obtaincard(numb_id)
            #print("\tXXXXXX", numb_id, "  ==>  ", card_O.ret_state())
            if card_O.ret_state() == "hidden":
                control_mouse[0] = -1
                advance_mouse[0] = -1
                #print("\tAdvance Grab work but card is hidden")
                return False
            
            #print("Special Advancee Grab => ", advance_mouse[0])

            return True
        elif collectionU[i0].grab_c(loc[0], loc[1]):
            numb_id= 0
            #print("\tXXXXXX",numb_id)
            control_mouse[0] = i0
            # global game_Omega
            numb_id = game_Omega[0].listSpare[control_mouse[0]][len(game_Omega[0].listSpare[control_mouse[0]])-1]
            card_O = game_Omega[0].obtaincard(numb_id)
            #print("\tXXXXXX", numb_id, "  ==>  ", card_O.ret_state())
            if card_O.ret_state() == "hidden":
                control_mouse[0] = -1
                #print("Grab work but card is hidden")
                return False
            # else:
                #print("\tGrab do happen")
            return True
        i0+=1
    return False

def move_to_Spare_deck(collectionU,  loc, card_id, control, control_mouse , advance_mouse ,mouse_symbol, score):
    
    if card_id == -99:
        symbol_numb = 0
        if mouse_symbol[0] == "Heart":
            symbol_numb = 9
        elif mouse_symbol[0] == "Clover":
            symbol_numb = 10
        elif mouse_symbol[0] == "Pica":
            symbol_numb = 11
        elif mouse_symbol[0] == "Diamond":
            symbol_numb=12
        
        
        #this section mean we are moving one or more cards from an spare deck into another spare	
        i0 =0
        while i0 < 7:
            if mouse_symbol[0] != "" and collectionU[i0].place_c(loc[0], loc[1]):
                #print("COLLECTION MOVE HAPPEN ON => ", i0)
                
                
                card_idX = game_Omega[0].obtainid_top_collection(mouse_symbol[0])
                #print("card id is ", card_idX)
                if game_Omega[0].to_Insert_Unorganize(card_idX, i0, symbol_numb ):
                    #print("\t\tSomething should happen XXX")
                    collectionU[i0].set_Quatity(len(game_Omega[0].listSpare[i0])) # rearange the quantity of the list Spare collection separattely to avodi unorganizatoin
                    coll_Heart.set_Quatity(len(game_Omega[0].listHeart))
                    coll_Pica.set_Quatity(len(game_Omega[0].listSpades))
                    coll_Diamond.set_Quatity(len(game_Omega[0].listDiamond))
                    coll_Clover.set_Quatity(len(game_Omega[0].listClover))
                    score[0] -= 10
                    
                    game_Omega[0].record_set()
                    return True
                return False
            
            i0+=1
        return True
    # if control is True, 
    # it mean we are moving a card from the Control deck to the Spare or Collection list
    if control == True:
        i0 =0
        while i0 < 7:
            if  collectionU[i0].place_c(loc[0], loc[1]):
                #print("CONTROL MOVE HAPPEN XXX")
                if game_Omega[0].to_Insert_Contol("Spare", i0 ):
                    #print("\tMovement should happen here")
                    collectionU[i0].set_Quatity(len(game_Omega[0].listSpare[i0]))
                    game_Omega[0].record_set()
                    score[0] += 5
                # else:
                #     print("\t Movement FAIL")
                
                return True
            i0+=1
        # /this section is toinserrt into collection list coming from control deck
        if coll_Heart.grab_special(loc[0], loc[1]):
                #print("\t HEART GREAT MOVE HAPPEN => ", card_id)
                #print("PRE List: ", game_Omega[0].listHeart)
                if game_Omega[0].to_Insert_Contol("Heart", 8):
                    #print("\tPOST List: ", game_Omega[0].listHeart)
                    coll_Heart.set_Quatity(len(game_Omega[0].listHeart))
                    game_Omega[0].record_set()
                    score[0] += 10
                # else:
                #     print("HEART to_insert fail")
                
        elif coll_Pica.grab_special(loc[0], loc[1]):
                #print("\t PICA GREAT MOVE HAPPEN => ", card_id)
                #print("PRE List: ", game_Omega[0].listSpades)
                if game_Omega[0].to_Insert_Contol("Spades", 8):
                    #print("\tSUPPER GREAT HAPPEN HAPPEN")
                    #print("\tPOST List: ", game_Omega[0].listSpades)
                    coll_Pica.set_Quatity(len(game_Omega[0].listSpades))
                    game_Omega[0].record_set()
                    score[0] += 10
                # else:
                #     print("PICA to_insert fail")
        elif coll_Diamond.grab_special(loc[0], loc[1]):
                #print("\tDIAMOND GREAT MOVE HAPPEN => ", card_id)
                #print("PRE List: ", game_Omega[0].listDiamond)
                if game_Omega[0].to_Insert_Contol( "Diamond", 8):
                    #print("\tSUPPER GREAT HAPPEN HAPPEN")
                    #print("\tPOST List: ", game_Omega[0].listDiamond)
                    coll_Diamond.set_Quatity(len(game_Omega[0].listDiamond))
                    game_Omega[0].record_set()
                    score[0] += 10
                # else:
                #     print("DIAMOND to_insert fail")
        elif coll_Clover.grab_special(loc[0], loc[1]):
                #print("\t CLOVER GREAT MOVE HAPPEN => ", card_id)
                #print("PRE List: ", game_Omega[0].listClover)
                if game_Omega[0].to_Insert_Contol("Clover", 8):
                    #print("\tPOST List: ", game_Omega[0].listClover)
                    coll_Clover.set_Quatity(len(game_Omega[0].listClover))
                    game_Omega[0].record_set()
                    score[0] += 10
                # else:
                #     print("CLOVER to_insert fail")

        return False
    
    #in case control isFalse and we are moving from one spare deck to the other spare deck
    i0 =0
    while i0 < 7:
        # this section isin case is fromone spare deck toanother spare deck
        # global control_mouse #control mouse signal the spare deck which you are holding (coming from)
        if i0!=control_mouse[0] and collectionU[i0].place_c(loc[0], loc[1]):
            #print("SPARE MOVE HAPPEN XXX")
            # if game_Omega[0].to_Insert_Unorganize(card_id, i0 , game_Omega[0].listSpare[control_mouse] ):
            if advance_mouse != -1:
                    #print("\t Advance_mouse happen XXX")
                    if game_Omega[0].to_Insert_Unorganize_long_section(control_mouse[0],i0,advance_mouse):
                        #print("\tADVANCE Movement should happen here")
                        collectionU[i0].set_Quatity(len(game_Omega[0].listSpare[i0])) # rearange the quantity of the list Spare collection separattely to avodi unorganizatoin
                        collectionU[control_mouse[0]].set_Quatity(len(game_Omega[0].listSpare[control_mouse[0]]))
                        
                        
                        # special step,revel if carrd behind is hidden
                        if advance_mouse-1 >=0:
                            card_O = game_Omega[0].deckA.deckZ[game_Omega[0].listSpare[control_mouse[0]][advance_mouse-1]]
                            if card_O.ret_state() == "hidden":
                                card_O.flip_card()
                                score[0] += 5
                            #     game_Omega[0].record_set()
                            # else:
                        game_Omega[0].record_set()
                        return True
                    else:
                        return False
            else:
                if game_Omega[0].to_Insert_Unorganize(card_id, i0 , control_mouse[0] ):
                    #print("\tMovement should happen here")
                    collectionU[i0].set_Quatity(len(game_Omega[0].listSpare[i0])) # rearange the quantity of the list Spare collection separattely to avodi unorganizatoin
                    collectionU[control_mouse[0]].set_Quatity(len(game_Omega[0].listSpare[control_mouse[0]]))
                    
                    
                    # special step,revel if carrd behind is hidden
                    if len(game_Omega[0].listSpare[control_mouse[0]])>0:
                        card_O = game_Omega[0].deckA.deckZ[game_Omega[0].listSpare[control_mouse[0]][len(game_Omega[0].listSpare[control_mouse[0]])-1]]
                        if card_O.ret_state() == "hidden":
                            card_O.flip_card()
                            score[0] += 5
                        #     game_Omega[0].record_set()
                        # else:
                    game_Omega[0].record_set()
                    
                    return True
                else:
                    #print("\t Movement FAIL")
                    return False
                
            return False
        
        i0+=1

    # /this section is to insert into collection list coming from spare deck
    if coll_Heart.grab_special(loc[0], loc[1]):
            #print("\t HEART GREAT MOVE HAPPEN vr 2=> ", card_id)
            #print("PRE List: ", game_Omega[0].listHeart)
            if game_Omega[0].to_Insert(card_grabbed_id[0], "Heart", control_mouse[0]):
                #print("\tSUPPER GREAT HAPPEN HAPPEN == Control M ==> ", control_mouse[0])
                #print("\tPOST List: ", game_Omega[0].listHeart)
                set_collection_quantity(collectionU) # rearange the quantity of the list Spare collection separattely to avodi unorganizatoin
                coll_Heart.set_Quatity(len(game_Omega[0].listHeart))
                score[0] += 10
                
                
                # special step,revel if carrd behind is hidden
                if len(game_Omega[0].listSpare[control_mouse[0]])>0:
                    #print("\t SPECIAL STEEPTO REVEALCARD")
                    card_O = game_Omega[0].deckA.deckZ[game_Omega[0].listSpare[control_mouse[0]][len(game_Omega[0].listSpare[control_mouse[0]])-1]]
                    if card_O.ret_state() == "hidden":
                        card_O.flip_card()
                        score[0] += 5
                    #     game_Omega[0].record_set()
                    # else:
                    game_Omega[0].record_set()
                else:
                    # print("\t SPECIAL STEP TO REVEAL CARD IS NOT HAPPENING, but movement do")
                    game_Omega[0].record_set()
            # else:
            #     print("HEART to_insert fail")
            
    elif coll_Pica.grab_special(loc[0], loc[1]):
            #print("\t PICA GREAT MOVE HAPPEN  vr 2 => ", card_id)
            #print("PRE List: ", game_Omega[0].listSpades)
            if game_Omega[0].to_Insert(card_grabbed_id[0], "Spades", control_mouse[0]):
                #print("\tSUPPER GREAT HAPPEN HAPPEN")
                #print("\tPOST List: ", game_Omega[0].listSpades)
                set_collection_quantity(collectionU) # rearrange the quantity of the list Spare collection separattely to avodi unorganizatoin
                coll_Pica.set_Quatity(len(game_Omega[0].listSpades))
                score[0] += 10
                
                # special step,revel if carrd behind is hidden
                if len(game_Omega[0].listSpare[control_mouse[0]]) > 0:
                    #print("\t SPECIAL STEEPTO REVEALCARD")
                    card_O = game_Omega[0].deckA.deckZ[ game_Omega[0].listSpare[control_mouse[0]][len(game_Omega[0].listSpare[control_mouse[0]])-1] ]
                    if card_O.ret_state() == "hidden":
                        card_O.flip_card()
                        score[0] += 5
                    #     game_Omega[0].record_set()
                    # else:
                    game_Omega[0].record_set()
                else:
                    # print("\t SPECIAL STEP TO REVEAL CARD IS NOOT HAPPENING, but movement do")
                    game_Omega[0].record_set()
            # else:
            #     print("PICA to_insert fail")
    elif coll_Diamond.grab_special(loc[0], loc[1]):
            #print("\tDIAMOND GREAT MOVE HAPPEN vr 2 => ", card_id)
            #print("PRE List: ", game_Omega[0].listDiamond)
            if game_Omega[0].to_Insert(card_grabbed_id[0], "Diamond", control_mouse[0]):
                #print("\tSUPPER GREAT HAPPEN HAPPEN")
                #print("\tPOST List: ", game_Omega[0].listDiamond)
                set_collection_quantity(collectionU) # rearrange the quantity of the list Spare collection separattely to avodi unorganizatoin
                coll_Diamond.set_Quatity(len(game_Omega[0].listDiamond))
                score[0] += 10
                
                # special step,revel if carrd behind is hidden
                if len(game_Omega[0].listSpare[control_mouse[0]]) > 0:
                    #print("\t SPECIAL STEEPTO REVEALCARD")
                    card_O = game_Omega[0].deckA.deckZ[game_Omega[0].listSpare[control_mouse[0]][len(game_Omega[0].listSpare[control_mouse[0]])-1]]
                    if card_O.ret_state() == "hidden":
                        card_O.flip_card()
                        score[0] += 5
                    #     game_Omega[0].record_set()
                    # else:
                    game_Omega[0].record_set()
                else:
                    # print("\t SPECIAL STEP TO REVEAL CARD IS NOOT HAPPENING, but momement do")
                    game_Omega[0].record_set()
            # else:
            #     print("DIAMOND to_insert fail")
    elif coll_Clover.grab_special(loc[0], loc[1]):
            #print("\t CLOVER GREAT MOVE HAPPEN vr 2 => ", card_id)
            #print("PRE List: ", game_Omega[0].listClover)
            if game_Omega[0].to_Insert(card_grabbed_id[0], "Clover", control_mouse[0]):
                #print("\tSUPPER GREAT HAPPEN HAPPEN == Control M ==> ", control_mouse[0])
                #print("\tPOST List: ", game_Omega[0].listClover)
                set_collection_quantity(collectionU) # rearrange the quantity of the list Spare collection separattely to avodi unorganizatoin
                coll_Clover.set_Quatity(len(game_Omega[0].listClover))
                score[0] += 10
                
                # special step,revel if carrd behind is hidden
                if len(game_Omega[0].listSpare[control_mouse[0]]) > 0:
                    #print("\t SPECIAL STEEPTO REVEALCARD")
                    card_O = game_Omega[0].deckA.deckZ[game_Omega[0].listSpare[control_mouse[0]][len(game_Omega[0].listSpare[control_mouse[0]])-1]]
                    if card_O.ret_state() == "hidden":
                        card_O.flip_card()
                        score[0] += 5
                    #     game_Omega[0].record_set()
                    # else:
                    game_Omega[0].record_set()
                else:
                    # print("\t SPECIAL STEP TO REVEAL CARD IS NOOT HAPPENING, but movement do")
                    game_Omega[0].record_set()
            # else:
            #     print("CLOVER to_insert fail")
    return False


def press_undo(loc):
    if loc[0] > 40 and loc[0] < 104:
        if loc[1] > 702 and loc[1] < 766:
            return True
    return False

def press_NEW_GAME(loc):
    if loc[0] > 792 and loc[0] < 856:
        if loc[1] > 702 and loc[1] < 766:
            return True
    return False

def start_new_game(loc):
    #result 1 mean YES
    #result 2 mean NO orpress outsidew the options
    #result 3 mean no option pressed
    if loc[0] > 312 and loc[0] < 429:
        if loc[1] > 381 and loc[1] < 418:
            return 1
    elif loc[0] > 482 and loc[0] < 598:
        if loc[1] > 380 and loc[1] < 419:
            return 2
    elif loc[0] < 250 or loc[0] > 650 or loc[1] < 200 or loc[1] > 456:
            return 2
    return 3



#set of object on location frospare decks
i0 = 0
collectionU = []
spare_loc = [20,160]
numbX = 120
while i0<7:
    collX = collection(spare_loc[0]+numbX*i0+numb, spare_loc[1])
    collectionU.append(collX)
    collectionU[i0].set_spare(i0)
    collectionU[i0].set_quantity(len(game_Omega[0].listSpare[i0]))
    i0+=1
    
def set_collection_quantity(collectionU):
    # rearange the quantity of the list Spare collection separattely to avodi unorganizatoin
    i0 =0
    while i0<7:
        collectionU[i0].set_quantity(len(game_Omega[0].listSpare[i0]))
        i0+=1
        

    
# setup the collection of card according to symbol
loc_collection = (790, 10) #any next piece is substract 90
iX= 90 #valy substrract for each different collection of cards
coll_Pica = collection(loc_collection[0], loc_collection[1])
coll_Pica.set_name("Pica")
coll_Pica.set_Quatity(len(game_Omega[0].listSpades))
coll_Heart = collection(loc_collection[0]-iX, loc_collection[1])
coll_Heart.set_name("Heart")
coll_Heart.set_Quatity(len(game_Omega[0].listHeart))
coll_Diamond = collection(loc_collection[0]-iX*2, loc_collection[1])
coll_Diamond.set_name("Diamond")
coll_Diamond.set_Quatity(len(game_Omega[0].listDiamond))
coll_Clover = collection(loc_collection[0]-iX*3, loc_collection[1])
coll_Clover.set_name("Clover")
coll_Clover.set_Quatity(len(game_Omega[0].listClover))

# set up collection of card controlling deck
coll_Control = collection(20, 10)
coll_Control.set_name("Control")
coll_Control.set_Quatity(0)

def collection_set_quantity(game_Omega, collectionU):
    #quick rearrange of size of collection and respective decks
    collectionU[0].set_Quatity(len(game_Omega[0].listSpare[0]))
    collectionU[1].set_Quatity(len(game_Omega[0].listSpare[1]))
    collectionU[2].set_Quatity(len(game_Omega[0].listSpare[2]))
    collectionU[3].set_Quatity(len(game_Omega[0].listSpare[3]))
    collectionU[4].set_Quatity(len(game_Omega[0].listSpare[4]))
    collectionU[5].set_Quatity(len(game_Omega[0].listSpare[5]))
    collectionU[6].set_Quatity(len(game_Omega[0].listSpare[6]))
    coll_Heart.set_Quatity(len(game_Omega[0].listHeart))
    coll_Pica.set_Quatity(len(game_Omega[0].listSpades))
    coll_Diamond.set_Quatity(len(game_Omega[0].listDiamond))
    coll_Clover.set_Quatity(len(game_Omega[0].listClover))

def undo_occurence(game_Omega, collectionU):
    game_Omega[0].undo_record()
    collection_set_quantity(game_Omega, collectionU)    

def new_game_press(game_Omega, collectionU):
    game_Omega[0].restart_game()
    collection_set_quantity(game_Omega, collectionU)

def game_complete():
    q_heart = coll_Heart.return_quantity()
    q_clover = coll_Clover.return_quantity()
    q_diamond = coll_Diamond.return_quantity()
    q_spades = coll_Pica.return_quantity()
    
    if q_heart  == q_diamond ==  q_clover == q_spades == 13:
        return True
    else:
        return False
    
def reset_controls(action_grabX, action_grab_controlX, 
                   action_grab_control_symbolX, control_mouseX, 
                   advance_mouseX, card_grabbed_idX, mouse_symbolX ):
    action_grabX[0]= False
    action_grab_controlX[0] = False
    action_grab_control_symbolX[0] = False
    control_mouseX[0] = -1
    advance_mouseX[0] = -1
    card_grabbed_idX[0] = -1
    mouse_symbolX[0] = ""

running = True
action_grab = [False] #grabbing a card from sparee_deck
action_grab_control = [False] #grabbing a card from control_deck
action_grab_control_symbol = [False] #grabbing a card from collection_deck
control_mouse = [-1] ##control mouse signal the spare deck which you are holding (coming from)
advance_mouse = [-1] #advance_mouse signal that you have taken several cards from the spare deck (how many carrds from)
card_grabbed_id = [-1] #signal the id of the carrd using at the movemnt

mouse_symbol = [""] #save the value of symbolcard collectited from symbol collection
new_game_set = [False]
score = [0] #This is the value of scorepoints in game
split_time = 0 #unneeceesary addition too add extra time on auto fill movemeent 

while running:
    
    mx, my = pygame.mouse.get_pos()
    rot = 0
    loc = [mx , my]
    
    #screen.blit(pygame.transform.rotate(img,rot),(loc[0]+offset_m[0], loc[1]+offset[1]))
    
    
    # #print("Super Array => ", gameX.array_illustration())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # print("location is ", loc)
                if new_game_set[0] == False:
                    if grab_spare_deck(game_Omega, collectionU, loc, control_mouse, advance_mouse):
                        #print("Grab card")
                        action_grab[0] = True
                    elif grab_control_deck(loc, game_Omega):
                        action_grab_control[0] = True
                        #print("Grab Control card")
                    elif grab_control_c(loc, mouse_symbol, loc_collection):
                        #print("Grab card from collection")
                        action_grab_control_symbol[0] = True
                    elif press_undo(loc):
                        # print("UNDO BUTTTON")
                        undo_occurence(game_Omega, collectionU)
                    elif press_NEW_GAME(loc):
                        new_game_set[0] = True
                        
                else:
                    set_fi = start_new_game(loc) #result of start_new_game, 1 mean YES, 2 mean NOour outsidee board, and 3 is null
                    if set_fi == 1:
                        # print("NEW GAME")
                        new_game_press(game_Omega, collectionU)
                        new_game_set[0] = False
                        score[0] = 0
                    elif set_fi == 2:
                        new_game_set[0] = False
                    elif set_fi == 3:
                        set_fi = 10
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                #print("Button rise")
                #print("\tLocation when button rise: ", loc) 
                if action_grab[0]== True:
                    # print("Grab and insert from spare")
                    move_to_Spare_deck(collectionU, loc, card_grabbed_id[0], False, control_mouse, advance_mouse[0] ,mouse_symbol, score)
                    reset_controls(action_grab, action_grab_control, action_grab_control_symbol, control_mouse, advance_mouse, card_grabbed_id, mouse_symbol)
                if action_grab_control[0] == True:
                    # print("Grab and insert from control")
                    move_to_Spare_deck(collectionU, loc, game_Omega[0].set_card_last(), True, control_mouse[0], -1 ,mouse_symbol, score)
                    reset_controls(action_grab, action_grab_control, action_grab_control_symbol, control_mouse, advance_mouse, card_grabbed_id, mouse_symbol )
                if action_grab_control_symbol[0] == True:
                    # print("Grab and insert from collection")
                    move_to_Spare_deck(collectionU, loc, -99, True, control_mouse[0] ,-1 , mouse_symbol, score)
                    reset_controls(action_grab, action_grab_control, action_grab_control_symbol, control_mouse, advance_mouse, card_grabbed_id, mouse_symbol )
            

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
            
            if event.key == pygame.K_a:
                print("Key a has been pressed")
                game_Omega[0].restart_game()

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
                print("Key i => Information")
                game_Omega[0].display_Length_of_game()
                
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
                game_Omega[0].print_records_length()
                
            if event.key == pygame.K_s:
                print("Key s has been pressed")
                game_Omega[0].display_Length_of_game()
                game_Omega[0].display_Length_of_Spare()
                
            if event.key == pygame.K_t:
                print("Key t has been pressed")
                game_Omega[0].print_set_up_game()
                
            if event.key == pygame.K_u:
                print("Key u has been pressed")
                undo_occurence(game_Omega, collectionU)

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
    
    #display spare deck
    if game_Omega[0].all_set_up() == False:
        if game_complete():
        # if True:
            congratulationX(180,100)
            display_collection(game_Omega , action_grab_control_symbol[0], mouse_symbol[0] ,loc)
            display_control_deck(game_Omega, loc, action_grab_control[0])
        else:
            if action_grab[0]== True: 
                display_collection(game_Omega , action_grab_control_symbol[0], mouse_symbol[0] ,loc)
                display_control_deck(game_Omega, loc, action_grab_control[0])
                display_spare_deck(game_Omega, collectionU,  loc, control_mouse, advance_mouse, card_grabbed_id)
            elif action_grab_control[0]== True: #grabbing a card from control_deck
                display_spare_deck(game_Omega, collectionU,  loc, control_mouse, advance_mouse, card_grabbed_id)
                display_collection(game_Omega , action_grab_control_symbol[0], mouse_symbol[0] ,loc)
                display_control_deck(game_Omega, loc, action_grab_control[0])
            else: 
                display_spare_deck(game_Omega, collectionU,  loc, control_mouse, advance_mouse, card_grabbed_id)
                display_control_deck(game_Omega, loc, action_grab_control[0])
                display_collection(game_Omega , action_grab_control_symbol[0], mouse_symbol[0] ,loc)
    else:
        if game_complete():
            congratulationX(180,100)
            display_collection(game_Omega , action_grab_control_symbol[0], mouse_symbol[0] ,loc)
            display_control_deck(game_Omega, loc, action_grab_control[0])
        else:
            if split_time == 4:
                if game_Omega[0].auto_complete_game():
                    # print("\tPiece Move")
                    collection_set_quantity(game_Omega, collectionU)
                    split_time = 0
                    score[0]+=10
            else:
                 split_time += 1   
            display_spare_deck(game_Omega, collectionU,  loc, control_mouse, advance_mouse, card_grabbed_id)
            display_collection(game_Omega , action_grab_control_symbol[0], mouse_symbol[0] ,loc)
            display_control_deck(game_Omega, loc, action_grab_control[0])

    if new_game_set[0] == True:
        board_new(250,200)
            
    undo_button(40, 702, loc)
    new_g__button(792, 702, loc)
    score_board(250, 725)
    
    set_numb(640, 725 ,score[0])
    
    

    
    pygame.display.update()
 