# import pygame
from pygame.locals import *
from download_control import *
import sys

# from .2048_SS.logicT import *
# complete path => /Users/failop/Projects/p2048/2048_SS
#complete path => 2048_SS
sys.path.append('../')
from solitary_logic import Solitary

pygame.init()


#title
pygame.display.set_caption("Solitary")
iconS = pygame.image.load("image/card_game.webp")
pygame.display.set_icon(iconS)

#size of the window
screen = pygame.display.set_mode((1000,800)) #height X:800  weight Y: 600
                    #start at left up corner


# how to set up a card from the deck on specific location
def card_set_up(pX,pY, id):
    global game_Omega
    card_O = game_Omega.obtaincard(id)
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
        
            
            
## SET UP GAME => seet up game object
game_Omega = Solitary()
game_Omega.set_up_game()
# game_Omega.manual_set_up_game()



print("Card Back width: ", card_back.get_width() )
print("Card Back height: ", card_back.get_height() )


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
    
    
def card_b2( pX,pY):
    global card_back
    card_back = pygame.transform.scale(card_back, (pX, pY))



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

numb = 50

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
    
    def set_name(self, new_name):
        self.name = new_name
    def set_Quatity(self, i0):
        self.quantity = i0
        print("\t New Quanttity is ",self.quantity)
            
            
    def display(self, dynamic, new_loc, hyper_dynamic, stage_s, i0):
        # dynamic refer if one card is on hnad
        #hyoper refer wheen seeveral hands are on hold
        #stage_S refer to  loocalization 
        if hyper_dynamic == False and dynamic == False:
            self.display_static(self.quantity,i0)
        elif hyper_dynamic:
            print("Hyper Dynamic")
            self.display_static(stage_s, i0)
            self.display_advance_dynamic(new_loc, stage_s, i0)
            # self.display_dynamic(new_loc)
        elif dynamic:
            self.display_static(self.quantity-1,  i0)
            self.display_dynamic(new_loc, i0)
            
    
    def ret_loc(self):
        return self.location
        
    def display_static(self, set_quantity, i02):
        # picture the the cards of list that stay in place 
        i0 = 0
        while i0 < set_quantity:
            # if state == hidden
            numb_id = game_Omega.listSpare[i02][i0]
            
            card_O = game_Omega.obtaincard(numb_id)
            if card_O.ret_state() == "reveal":
                card_set_up(self.location[0], self.location[1]+20*i0, numb_id)
            else:
                card_b(self.location[0], self.location[1]+20*i0)
            # card_b(self.location[0], self.location[1]+20*i0)
            i0 += 1
        
        
    def display_dynamic(self, new_loc, i0):
         # picture the the one card oof list that move with our hand 
        numb_id = game_Omega.listSpare[i0][len(game_Omega.listSpare[i0])-1]
        global card_grabbed_id
        card_grabbed_id = numb_id
        card_set_up(new_loc[0]-40, new_loc[1]-53, numb_id )
        # card_b(new_loc[0]-40, new_loc[1]-53)
        
    def display_advance_dynamic(self, new_loc, stage_s, spare_numb):
         # picture the X's cards of list that movee with our mouse
        # print("\tself.quatity => ", self.quantity) 
        # print("\tstagee_s => ", stage_s) 
        i0 = self.quantity - stage_s
        i02 = 0
        while i02 < i0:
            numb_id = game_Omega.listSpare[spare_numb][i02+stage_s]
            card_set_up(new_loc[0]-40, new_loc[1]-53+20*i02,numb_id )
            i02+=1
    
        
        
    def display_special(self, conditionX, symbol_name, new_loc):
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
                        card_set_up(new_loc[0]-40, new_loc[1]-53, 0)
                    else:
                        card_set_up(self.location[0], self.location[1], 0)
                else:
                    card_set_up(self.location[0], self.location[1], self.quantity-2)
                    if conditionX == True and symbol_name == self.name:
                        card_set_up(new_loc[0]-40, new_loc[1]-53, self.quantity-1)
                    else:
                        card_set_up(self.location[0], self.location[1], self.quantity-1)
                    # card_set_up(self.location[0], self.location[1], self.quantity-1)
            elif self.name == "Heart":
                if self.quantity -1 == 0:
                    card_Heart(self.location[0], self.location[1])
                    if conditionX == True and symbol_name == self.name:
                        card_set_up(new_loc[0]-40, new_loc[1]-53, 39)
                    else:
                        card_set_up(self.location[0], self.location[1], 39)
                else:
                    card_set_up(self.location[0], self.location[1], self.quantity-2+39)
                    if conditionX == True and symbol_name == self.name:
                        card_set_up(new_loc[0]-40, new_loc[1]-53, self.quantity-1+39)
                    else:
                        card_set_up(self.location[0], self.location[1], self.quantity-1+39)
                    # card_set_up(self.location[0], self.location[1], self.quantity-1+39)
            elif self.name == "Pica":
                if self.quantity -1 == 0:
                    card_Pica(self.location[0], self.location[1])
                    if conditionX == True and symbol_name == self.name:
                        card_set_up(new_loc[0]-40, new_loc[1]-53, 26)
                    else:
                        card_set_up(self.location[0], self.location[1], 26)
                    # card_set_up(self.location[0], self.location[1], 26)
                else:
                    card_set_up(self.location[0], self.location[1], self.quantity-2+26)
                    if conditionX == True and symbol_name == self.name:
                        card_set_up(new_loc[0]-40, new_loc[1]-53, self.quantity-1+26)
                    else:
                        card_set_up(self.location[0], self.location[1], self.quantity-1+26)
                    # card_set_up(self.location[0], self.location[1], self.quantity-1+26)
            elif self.name == "Diamond":
                if self.quantity -1 == 0:
                    card_Diamond(self.location[0], self.location[1])
                    # card_set_up(self.location[0], self.location[1], 13)
                    if conditionX == True and symbol_name == self.name:
                        card_set_up(new_loc[0]-40, new_loc[1]-53, 13)
                    else:
                        card_set_up(self.location[0], self.location[1], 13)
                else:
                    card_set_up(self.location[0], self.location[1], self.quantity-2+13)
                    if conditionX == True and symbol_name == self.name:
                        card_set_up(new_loc[0]-40, new_loc[1]-53, self.quantity-1+13)
                    else:
                        card_set_up(self.location[0], self.location[1], self.quantity-1+13)
                    # card_set_up(self.location[0], self.location[1], self.quantity-1+13)
        
            
        
    def move_loc(self, new_loc):
        self.location = new_loc 
        
    def grab_control_d(self, px, py):
        # grab control deck mean that if you press the deck 
        # we could deal with display cards 
        i0 = 2
        ix = 120+i0*20
        if px >= 20 and px <= 20+80:
            if py >=10 and py<=10+105:
                print("You have press the DECK")
                return True
        return  False


    
    def grab_control_m(self, px, py):
        # grab control maneable mean 
        # that you are dealing with the card tht can be move around
        i0 = 2
        ix = 120+i0*20
        if px >= ix and px <= ix+80:
            if py >= 10 and py <= 10+105:
                print("YOU HAVE GRAB CONTROL")
                return True
        return  False
    
    def grab_advance(self,px,py, spare_num ,list_k):
        #meethod on colleection to verify is advanse_mouse can bee apply
        #list_k: list where will be save the number of the list
        i0 = self.quantity-1
        if px >= self.location[0] and px <= self.location[0]+80:
            #grab any card aboove the last card
            if i0+1 > 1:
                while i0 > 0:
                    if py < self.location[1]+20*i0 and py >= self.location[1]+20*(i0-1):
                        global game_Omega
                        if game_Omega.check_list_Unorganize(spare_num, i0-1):
                            print("Advance Grab card == spare_num: ", spare_num, "\t i0: ",i0-1)
                            list_k[0] = (i0-1)
                            return True
                        else:
                            print("You grab card, but it is not unoganize")
                            return False
                    i0-=1
        return False
        
    def grab_c(self,px,py):
        i0 = self.quantity-1
        # print("Self quantity: ", i0+1)
        if px >= self.location[0] and px <= self.location[0]+80:
            #grab last card
            if py >= self.location[1]+20*i0 and py <= self.location[1]+20*i0+105:
                print("Super Grab card")
                return True
        return False
    
    def place_c(self,px,py):
        i0 = self.quantity-1
        print("Self quantity: ", i0+1)
        if px >= self.location[0] and px <= self.location[0]+80:
            #grab last card
            if py >= self.location[1]+20*i0 and py <= self.location[1]+20*i0+105:
                print("Super Grab card")
                return True
        return False
    
    def grab_special(self,px,py):
        if px >= self.location[0] and px <= self.location[0]+80:
            #grab last card
            if py >= self.location[1] and py <= self.location[1]+105:
                print("Super Grab card")
                return True
        return False
    


def Grab_column(loc , control_mouse):
    control_mouse[0] = 1
    return coll1.grab_c(loc[0],loc[1])


def grab_control_c(loc, cc):
    # grab control collection meean that if you press the collection 
    # so know we can grab deetermine card 
    py = loc[1]
    px = loc[0]
    if py >=10 and py<=10+105:
        if px >= 900 and px <= 900+80:
            cc[0] = "Pica"
            print("You have press the collection of Pica => ", cc)
            return True
        elif px >= 810 and px <= 810+80:
            cc[0] = "Heart"
            print("You have press the collection of Heart")
            return True
        elif px >= 720 and px <= 720+80:
            cc[0] = "Diamond"
            print("You have press the collection of Diamond")
            return True
        elif px >= 630 and px <= 630+80:
            cc[0] = "Clover"
            print("You have press the collection of Clover")
            return True
    return  False

#set of object on location frospare decks
i0 = 0
collectionU = []
spare_loc = [20,160]
numbX = 120
while i0<7:
    collX = collection(spare_loc[0]+numbX*i0+numb, spare_loc[1])
    collectionU.append(collX)
    collectionU[i0].set_spare(i0)
    collectionU[i0].set_quantity(len(game_Omega.listSpare[i0]))
    i0+=1
    
def set_collection_quantity():
    # rearange the quantity of the list Spare collection separattely to avodi unorganizatoin
    i0 =0
    while i0<7:
        collectionU[i0].set_quantity(len(game_Omega.listSpare[i0]))
        i0+=1
        

    
# setup the collection of card according to symbol
coll_Pica = collection(900, 10)
coll_Pica.set_name("Pica")
coll_Pica.set_Quatity(0)
coll_Heart = collection(810, 10)
coll_Heart.set_name("Heart")
coll_Heart.set_Quatity(0)
coll_Diamond = collection(720,10)
coll_Diamond.set_name("Diamond")
coll_Diamond.set_Quatity(0)
coll_Clover = collection(630, 10)
coll_Clover.set_name("Clover")
coll_Clover.set_Quatity(0)

# set up collection of card controlling deck
coll_Control = collection(20, 10)
coll_Control.set_name("Control")
coll_Control.set_Quatity(0)


def display_spare_deck(loc, control_mouse, advance_mouse):
    i0 = 0
    while i0<7:
        if i0 == control_mouse[0]:
            if advance_mouse[0] != -1:
                print("SUPER ADVANCE MOUSE BUTTON")
                collectionU[i0].display(True, loc, True, advance_mouse[0], i0)
            else:
                collectionU[i0].display(True, loc, False, -1, i0)
        else:
            collectionU[i0].display(False, loc, False, -1,i0)
        i0+=1
    
def display_collection(grab_happen, symbol_name, new_loc):
    coll_Pica.display_special(grab_happen, symbol_name ,new_loc)
    coll_Clover.display_special(grab_happen, symbol_name ,new_loc)
    coll_Diamond.display_special(grab_happen, symbol_name ,new_loc)
    coll_Heart.display_special(grab_happen, symbol_name ,new_loc)
    
    
def display_control_deck(loc, grab):
    display_control(loc, grab)
    
def display_control(new_loc, grab):
    i0 = len(game_Omega.listControl)-game_Omega.setcount
    if i0 <= 0:
        screen.blit(card_empty ,(20, 10))
    else:
        card_b(20,10)
    listK = game_Omega.set_card()
    i02 = len(listK)
    i03 = 0
    if grab == True:
        i02 = i02-1
    while i03< i02:
        card_set_up(120+i03*20,10, listK[i03])
        i03+=1
    if grab == True:
        card_set_up(new_loc[0]-40, new_loc[1]-53+20*i02, listK[len(listK)-1])

def grab_control_deck(self):
    if coll_Control.grab_control_d(loc[0], loc[1]):
        print("\t GRAB DEECK ==> THEREFORE EXPAND CARDS")
        game_Omega.set_control()
        print("\t\t this is the new control count ",  game_Omega.setcount)
    elif coll_Control.grab_control_m(loc[0], loc[1]):
        print("\t GRAB EXTRA DECK ==> THEREFORE manage CARDS")
        return True
    return False

def grab_spare_deck(loc, control_mouse, advance_mouse):
    i0 = 0
    while i0 < 7:
        list_k= [-1]
        # global control_mouse
        if collectionU[i0].grab_advance(loc[0], loc[1], i0 ,list_k):
            control_mouse[0] = i0
            advance_mouse[0] = list_k[0]
            list_k.clear()
            
            numb_id = game_Omega.listSpare[control_mouse[0]][advance_mouse[0]]
            card_O = game_Omega.obtaincard(numb_id)
            print("\tXXXXXX", numb_id, "  ==>  ", card_O.ret_state())
            if card_O.ret_state() == "hidden":
                control_mouse[0] = -1
                advance_mouse[0] = -1
                print("\tAdvance Grab work but card is hidden")
                return False
            
            print("Special Advancee Grab => ", advance_mouse[0])

            return True
        elif collectionU[i0].grab_c(loc[0], loc[1]):
            numb_id= 0
            print("\tXXXXXX",numb_id)
            control_mouse[0] = i0
            # global game_Omega
            numb_id = game_Omega.listSpare[control_mouse[0]][len(game_Omega.listSpare[control_mouse[0]])-1]
            card_O = game_Omega.obtaincard(numb_id)
            print("\tXXXXXX", numb_id, "  ==>  ", card_O.ret_state())
            if card_O.ret_state() == "hidden":
                control_mouse[0] = -1
                print("Grab work but card is hidden")
                return False
            else:
                print("\tGrab do happen")
            return True
        i0+=1
    return False

def move_to_Spare_deck(loc, card_id, control, control_mouse , advance_mouse ,mouse_symbol):
    
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
        
        
        #this section mean we are moving one or more cards from an spare deck into another collection	
        i0 =0
        while i0 < 7:
            if mouse_symbol[0] != "" and collectionU[i0].place_c(loc[0], loc[1]):
                print("COLLECTION MOVE HAPPEN ON => ", i0)
                
                
                card_idX = game_Omega.obtainid_top_collection(mouse_symbol[0])
                print("card id is ", card_idX)
                if game_Omega.to_Insert_Unorganize(card_idX, i0, symbol_numb ):
                    print("\t\tSomething should happen XXX")
                    collectionU[i0].set_Quatity(len(game_Omega.listSpare[i0])) # rearange the quantity of the list Spare collection separattely to avodi unorganizatoin
                    coll_Heart.set_Quatity(len(game_Omega.listHeart))
                    coll_Pica.set_Quatity(len(game_Omega.listSpades))
                    coll_Diamond.set_Quatity(len(game_Omega.listDiamond))
                    coll_Clover.set_Quatity(len(game_Omega.listClover))
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
                print("CONTROL MOVE HAPPEN XXX")
                if game_Omega.to_Insert_Contol("Spare", i0 ):
                    print("\tMovement should happen here")
                    collectionU[i0].set_Quatity(len(game_Omega.listSpare[i0]))
                else:
                    print("\t Movement FAIL")
                
                return True
            i0+=1
        # /this section is toinserrt into collection list coming from control deck
        if coll_Heart.grab_special(loc[0], loc[1]):
                print("\t HEART GREAT MOVE HAPPEN => ", card_id)
                print("PRE List: ", game_Omega.listHeart)
                if game_Omega.to_Insert_Contol("Heart", 8):
                    print("\tPOST List: ", game_Omega.listHeart)
                    coll_Heart.set_Quatity(len(game_Omega.listHeart))
                else:
                    print("HEART to_insert fail")
                
        elif coll_Pica.grab_special(loc[0], loc[1]):
                print("\t PICA GREAT MOVE HAPPEN => ", card_id)
                print("PRE List: ", game_Omega.listSpades)
                if game_Omega.to_Insert_Contol("Spades", 8):
                    print("\tSUPPER GREAT HAPPEN HAPPEN")
                    print("\tPOST List: ", game_Omega.listSpades)
                    coll_Pica.set_Quatity(len(game_Omega.listSpades))
                else:
                    print("PICA to_insert fail")
        elif coll_Diamond.grab_special(loc[0], loc[1]):
                print("\tDIAMOND GREAT MOVE HAPPEN => ", card_id)
                print("PRE List: ", game_Omega.listDiamond)
                if game_Omega.to_Insert_Contol( "Diamond", 8):
                    print("\tSUPPER GREAT HAPPEN HAPPEN")
                    print("\tPOST List: ", game_Omega.listDiamond)
                    coll_Diamond.set_Quatity(len(game_Omega.listDiamond))
                else:
                    print("DIAMOND to_insert fail")
        elif coll_Clover.grab_special(loc[0], loc[1]):
                print("\t CLOVER GREAT MOVE HAPPEN => ", card_id)
                print("PRE List: ", game_Omega.listClover)
                if game_Omega.to_Insert_Contol("Clover", 8):
                    print("\tPOST List: ", game_Omega.listClover)
                    coll_Clover.set_Quatity(len(game_Omega.listClover))
                else:
                    print("CLOVER to_insert fail")

        return False
    
    #in case control isFalse and we are moving from one spare deck to the other spare deck
    i0 =0
    while i0 < 7:
        # this section isin case is fromone spare deck toanother spare deck
        # global control_mouse #control mouse signal the spare deck which you are holding (coming from)
        if i0!=control_mouse[0] and collectionU[i0].place_c(loc[0], loc[1]):
            print("SPARE MOVE HAPPEN XXX")
            # if game_Omega.to_Insert_Unorganize(card_id, i0 , game_Omega.listSpare[control_mouse] ):
            if advance_mouse != -1:
                    print("\t Advance_mouse happen XXX")
                    if game_Omega.to_Insert_Unorganize_long_section(control_mouse[0],i0,advance_mouse):
                        print("\tADVANCE Movement should happen here")
                        collectionU[i0].set_Quatity(len(game_Omega.listSpare[i0])) # rearange the quantity of the list Spare collection separattely to avodi unorganizatoin
                        collectionU[control_mouse[0]].set_Quatity(len(game_Omega.listSpare[control_mouse[0]]))
                        
                        # special step,revel if carrd behind is hidden
                        if advance_mouse-1 >=0:
                            card_O = game_Omega.deckA.deckZ[game_Omega.listSpare[control_mouse[0]][advance_mouse-1]]
                            if card_O.ret_state() == "hidden":
                                card_O.flip_card()
                        return True
                    else:
                        return False
            else:
                if game_Omega.to_Insert_Unorganize(card_id, i0 , control_mouse[0] ):
                    print("\tMovement should happen here")
                    collectionU[i0].set_Quatity(len(game_Omega.listSpare[i0])) # rearange the quantity of the list Spare collection separattely to avodi unorganizatoin
                    collectionU[control_mouse[0]].set_Quatity(len(game_Omega.listSpare[control_mouse[0]]))
                    
                    # special step,revel if carrd behind is hidden
                    if len(game_Omega.listSpare[control_mouse[0]])>0:
                        card_O = game_Omega.deckA.deckZ[game_Omega.listSpare[control_mouse[0]][len(game_Omega.listSpare[control_mouse[0]])-1]]
                        if card_O.ret_state() == "hidden":
                            card_O.flip_card()
                    
                    return True
                else:
                    print("\t Movement FAIL")
                    return False
                
            return False
        
        i0+=1

    # /this section is to insert into collection list coming from spare deck
    if coll_Heart.grab_special(loc[0], loc[1]):
            print("\t HEART GREAT MOVE HAPPEN vr 2=> ", card_id)
            print("PRE List: ", game_Omega.listHeart)
            if game_Omega.to_Insert(card_grabbed_id, "Heart", control_mouse[0]):
                print("\tSUPPER GREAT HAPPEN HAPPEN == Control M ==> ", control_mouse[0])
                print("\tPOST List: ", game_Omega.listHeart)
                set_collection_quantity() # rearange the quantity of the list Spare collection separattely to avodi unorganizatoin
                coll_Heart.set_Quatity(len(game_Omega.listHeart))
                
                # special step,revel if carrd behind is hidden
                if len(game_Omega.listSpare[control_mouse[0]])>0:
                    print("\t SPECIAL STEEPTO REVEALCARD")
                    card_O = game_Omega.deckA.deckZ[game_Omega.listSpare[control_mouse[0]][len(game_Omega.listSpare[control_mouse[0]])-1]]
                    if card_O.ret_state() == "hidden":
                        card_O.flip_card()
                else:
                    print("\t SPECIAL STEP TO REVEAL CARD IS NOOT HAPPENING")
            else:
                print("HEART to_insert fail")
            
    elif coll_Pica.grab_special(loc[0], loc[1]):
            print("\t PICA GREAT MOVE HAPPEN  vr 2 => ", card_id)
            print("PRE List: ", game_Omega.listSpades)
            if game_Omega.to_Insert(card_grabbed_id, "Spades", control_mouse[0]):
                print("\tSUPPER GREAT HAPPEN HAPPEN")
                print("\tPOST List: ", game_Omega.listSpades)
                set_collection_quantity() # rearrange the quantity of the list Spare collection separattely to avodi unorganizatoin
                coll_Pica.set_Quatity(len(game_Omega.listSpades))
                
                # special step,revel if carrd behind is hidden
                if len(game_Omega.listSpare[control_mouse[0]]) > 0:
                    print("\t SPECIAL STEEPTO REVEALCARD")
                    card_O = game_Omega.deckA.deckZ[ game_Omega.listSpare[control_mouse[0]][len(game_Omega.listSpare[control_mouse[0]])-1] ]
                    if card_O.ret_state() == "hidden":
                        card_O.flip_card()
                else:
                    print("\t SPECIAL STEP TO REVEAL CARD IS NOOT HAPPENING")
            else:
                print("PICA to_insert fail")
    elif coll_Diamond.grab_special(loc[0], loc[1]):
            print("\tDIAMOND GREAT MOVE HAPPEN vr 2 => ", card_id)
            print("PRE List: ", game_Omega.listDiamond)
            if game_Omega.to_Insert(card_grabbed_id, "Diamond", control_mouse[0]):
                print("\tSUPPER GREAT HAPPEN HAPPEN")
                print("\tPOST List: ", game_Omega.listDiamond)
                set_collection_quantity() # rearrange the quantity of the list Spare collection separattely to avodi unorganizatoin
                coll_Diamond.set_Quatity(len(game_Omega.listDiamond))
                
                # special step,revel if carrd behind is hidden
                if len(game_Omega.listSpare[control_mouse[0]]) > 0:
                    print("\t SPECIAL STEEPTO REVEALCARD")
                    card_O = game_Omega.deckA.deckZ[game_Omega.listSpare[control_mouse[0]][len(game_Omega.listSpare[control_mouse[0]])-1]]
                    if card_O.ret_state() == "hidden":
                        card_O.flip_card()
                else:
                    print("\t SPECIAL STEP TO REVEAL CARD IS NOOT HAPPENING")
            else:
                print("DIAMOND to_insert fail")
    elif coll_Clover.grab_special(loc[0], loc[1]):
            print("\t CLOVER GREAT MOVE HAPPEN vr 2 => ", card_id)
            print("PRE List: ", game_Omega.listClover)
            if game_Omega.to_Insert(card_grabbed_id, "Clover", control_mouse[0]):
                print("\tSUPPER GREAT HAPPEN HAPPEN == Control M ==> ", control_mouse[0])
                print("\tPOST List: ", game_Omega.listClover)
                set_collection_quantity() # rearrange the quantity of the list Spare collection separattely to avodi unorganizatoin
                coll_Clover.set_Quatity(len(game_Omega.listClover))
                
                # special step,revel if carrd behind is hidden
                if len(game_Omega.listSpare[control_mouse[0]]) > 0:
                    print("\t SPECIAL STEEPTO REVEALCARD")
                    card_O = game_Omega.deckA.deckZ[game_Omega.listSpare[control_mouse[0]][len(game_Omega.listSpare[control_mouse[0]])-1]]
                    if card_O.ret_state() == "hidden":
                        card_O.flip_card()
                else:
                    print("\t SPECIAL STEP TO REVEAL CARD IS NOOT HAPPENING")
            else:
                print("CLOVER to_insert fail")
    return False

        




running = True
action_grab = False
action_grab_control = False
action_grab_control_symbol = False
control_mouse = [-1] ##control mouse signal the spare deck which you are holding (coming from)
advance_mouse = [-1] #advance_mouse signal that you have taken several cards from the spare deck (how many carrds from)
card_grabbed_id = -1 #signal the id of the carrd using at the movemnt

mouse_symbol = [""] #save the value of symbolcard collectited from symbol collection

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
                if grab_spare_deck(loc, control_mouse, advance_mouse):
                    print("Grab card")
                    action_grab = True
                elif grab_control_deck(loc):
                    action_grab_control = True
                    print("Grab Control card")
                elif grab_control_c(loc, mouse_symbol):
                    print("Grab card from collection")
                    action_grab_control_symbol = True
            # if event.button == 3:
            #     print("I don't know => Right click")
            # if event.button == 4:
            #     print("I don't know => midddle click")
            # if event.button == 5:
            #     print("I don't know => not middle click")
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                print("Button rise")
                print("\tLocation when button rise: ", loc) 
                if action_grab == True:
                    move_to_Spare_deck(loc, card_grabbed_id, False, control_mouse, advance_mouse[0] ,mouse_symbol)
                    action_grab = False
                    action_grab_control = False
                    action_grab_control_symbol = False
                    control_mouse[0] = -1
                    advance_mouse[0] = -1
                    card_grabbed_id = -1
                    mouse_symbol[0] = ""
                if action_grab_control == True:
                    move_to_Spare_deck(loc, game_Omega.set_card_last(), True, control_mouse, -1 ,mouse_symbol)
                    action_grab = False
                    action_grab_control = False
                    action_grab_control_symbol = False
                    control_mouse[0] = -1
                    advance_mouse[0] = -1
                    card_grabbed_id = -1
                    mouse_symbol[0] = ""
                if action_grab_control_symbol == True:
                    move_to_Spare_deck(loc, -99, True, control_mouse ,-1 , mouse_symbol)
                    # print("Hello Omega GGG")
                    action_grab = False
                    action_grab_control = False
                    action_grab_control_symbol = False
                    control_mouse[0] = -1
                    advance_mouse[0] = -1
                    card_grabbed_id = -1
                    mouse_symbol[0] = ""
            

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
                print("Key i => Information")
                game_Omega.display_Length_of_game()
                
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
                game_Omega.display_Length_of_game()
                game_Omega.display_Length_of_Spare()
                
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
    # card_b(20,10)
    # card_b(1100,10)
    
    #display spare deck
    display_collection(action_grab_control_symbol, mouse_symbol[0] ,loc)
    display_spare_deck(loc, control_mouse, advance_mouse)
    display_control_deck(loc, action_grab_control)
    
    

    
    pygame.display.update()
 