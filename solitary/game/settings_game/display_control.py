# import pygame
from ..game import save_screen

screen = save_screen()

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