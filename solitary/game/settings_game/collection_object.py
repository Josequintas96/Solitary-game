from .display_control import *

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
            print("Dynamic")
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
 