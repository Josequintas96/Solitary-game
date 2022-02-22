from  deck_logic import *
from record import *

class Solitary():
	deckA = None
	setcount = [0] #variable to manage the three cards present in front
	list_set = []
	listControl = [] #deck at hand
	listClover = [] #accumulation of clover cards
	listDiamond = [] #accumulation of Diamond cards
	listSpades = [] #accumulation of Spades cards
	listHeart = [] #accumulation of Heart cards
	listSpare = []

	recordA = None
 
	
	def __init__(self):
		self.deckA = Deck()
		self.recordA = Record()
		self.deckA.share_deck(self.listControl)
		i0 = 0
		while i0<7:
			extra_list = []
			self.listSpare.append(extra_list)
			i0+=1

	def print_records_length(self):
		self.recordA.print_record()
  
	def print_set_up_game(self):
		# self.listControl = [0,1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24]
		print("\tControl: ", self.listControl )
		print("\tHeart: ", self.listHeart )
		print("\tDiamond: ", self.listDiamond)
		print("\tSpade: ", self.listSpades )
		print("\tClover: ", self.listClover )
		print("\tSpare 0: ", self.listSpare[0])
		print("\tSpare 1: ", self.listSpare[1])
		print("\tSpare 2: ", self.listSpare[2])
		print("\tSpare 3: ", self.listSpare[3])
		print("\tSpare 4: ", self.listSpare[4])
		print("\tSpare 5: " ,self.listSpare[6])
		print("\tSpare 6: " ,self.listSpare[6])
    
	def record_set(self):
		#save actual statee of the lists of game
		print("\tSET UP RECORD")
		self.recordA.set_record(self.deckA, self.listControl, self.listClover, self.listHeart, self.listSpades, self.listDiamond, self.listSpare, self.setcount)

	def undo_record(self):
		#restttortto previous stage of deck
		self.recordA.restort_record(self.deckA, self.listControl, self.listClover, self.listHeart, self.listSpades, self.listDiamond, self.listSpare, self.setcount)


	def manual_set_up_game(self):
		# self.listControl = [0,1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24]
		self.listControl = [51,50,49,48,47,46,
					  38,37,36,35,34,33,
					  25,24,23,22,21,20,
					  12,11,10,9,8,7]
		self.listSpare[0] = [0]
		self.listSpare[1] = [2,1]
		self.listSpare[2] = [5,4,3]
		self.listSpare[3] = [15,14,13,6]
		self.listSpare[4] = [26,19,18,17,16]
		self.listSpare[5] = [32,31,30,29,28,27]
		self.listSpare[6] = [45,44,43,42,41,40,39]
		self.manual_set_up_spare_deck()
		self.record_set()

  
	def manual_set_up_game4(self):
		# self.listControl = [0,1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24]
		self.listControl = [51,50,49,48,47,46,
					  38,37,36,35,34,33,
					  25,24,23,22,21,20,
					  12,11,10,9,8,7]
		self.listSpare[0] = [0]
		self.listSpare[1] = [2,1]
		self.listSpare[2] = [5,4,3]
		self.listSpare[3] = [15,14,13,6]
		self.listSpare[4] = [26,19,18,17,16]
		self.listSpare[5] = [32,31,30,29,28,27]
		self.listSpare[6] = [45,44,43,42,41,40,39]
		self.manual_set_up_spare_deck()
		self.record_set()
  
	def manual_set_up_game2(self):
		# self.listControl = [0,1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24]
		self.listControl = [10,3,46,
					  		7,39,34,
							20,12,0,
						 	25,42,33,
						  	8,41,16
						  	]
		self.listSpare[0] = []
		self.listSpare[1] = []
		self.listSpare[2] = []
		self.listSpare[3] = []
		self.listSpare[4] = []
		self.listSpare[5] = []
		self.listSpare[6] = []
		self.listClover = []
		self.listDiamond = []
		self.listHeart = []
		self.listSpades = []
		self.manual_set_up_spare_deck()
		self.record_set()

	def manual_set_up_game5(self):
		self.listControl = []
		self.listSpare[0] = [12]
		self.listSpare[1] = [24]
		self.listSpare[2] = [10]
		self.listSpare[3] = []
		self.listSpare[4] = []
		self.listSpare[5] = [51]
		self.listSpare[6] = [38,50,36,48]
		self.listClover = []
		self.listDiamond = []
		self.listHeart = []
		self.listSpades = []
		self.manual_set_up_spare_deck()
		self.record_set()

  
	def manual_set_up_game3(self):
		# self.listControl = [0,1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24]
		self.listControl = []
		self.listSpare[0] = [30, 2]
		self.listSpare[1] = [25,16, 14,26]
		self.listSpare[2] = []
		self.listSpare[3] = []
		self.listSpare[4] = []
		self.listSpare[5] = []
		self.listSpare[6] = []
		self.listClover = []
		self.listDiamond = []
		self.listHeart = []
		self.listSpades = []
		self.manual_set_up_spare_deck()
		self.record_set()
  
	def manual_set_up_spare_deck(self):
		i0 =0
		while i0 < 7:
			i2 =0
			i3 = len(self.listSpare[i0])
			while i2 < i3:
				i_add = self.listSpare[i0][i2]
				self.deckA.deckZ[i_add].flip_back()
				i2+=1
			if i2-1 >=0 and i2-1< i3:
				#print("\t\tThis is i2: ",i2-1, " and i3 ", i3)
				i_add = self.listSpare[i0][i2-1]
				self.deckA.deckZ[i_add].flip_card()
			i0+=1
		#print()


	def set_up_game(self):
		self.shuffle_Control()
		self.set_up_spare_deck()
		self.record_set()
  
	def set_up_spare_deck(self):
		i0 =0
		while i0 < 7:
			i02 =0
			while i02 < i0+1:
				i_add = self.listControl[0]
				self.move_to( self.listControl, self.listSpare[i0], i_add)
				self.deckA.deckZ[i_add].flip_back()
				i02+=1
			i_add = self.listSpare[i0][i02-1]
			self.deckA.deckZ[i_add].flip_card()
			self.shuffle_Control()
			i0+=1
		#print()

	def restart_game(self):
		self.deckA.set_reveal_all_deck()
		self.clean_all_list()
		self.setcount[0] = 0
		self.deckA.share_deck(self.listControl)
  
		# del self.recordA
		# self.recordA = Record()
		self.recordA.reset_record()
		self.set_up_game()

  
	def clean_all_list(self):
		self.listClover.clear()
		self.listDiamond.clear()
		self.listSpades.clear()
		self.listHeart.clear()
		self.listControl.clear()
		for i0 in self.listSpare:
			i0.clear()
		

	def all_set_up(self):
    # autocomplete the game
    # this is a method to mark that all control has beeing arrange 
    #... and to mark that all cards in sparre has being reveal
		if len(self.listControl) == 0:
			print("Control has being completely arrange")
			
		return False


	def displayDeck(self):
		self.deckA.displayControlDeck(self.listControl)

	def displayDeck_Clover(self):
		self.deckA.displayControlDeck(self.listClover)

	def displayDeck_Heart(self):
		self.deckA.displayControlDeck(self.listHeart)

	def displayDeck_Diamond(self):
		self.deckA.displayControlDeck(self.listDiamond)

	def displayDeck_Spades(self):
		self.deckA.displayControlDeck(self.listSpades)

	def displayDeck_Spare(self,number):
		if number < 7:
			self.deckA.displayControlDeck(self.listSpare[number])

			

	def display_Length_of_game(self):
		#set control of how many cards have the 5 sections of the game
		print("Lenght of main Deck: ", len(self.listControl))
		print("Lenght of Heart Deck: ", len(self.listHeart))
		print("Lenght of Diamond Deck: ", len(self.listDiamond))
		print("Lenght of Clover Deck: ", len(self.listClover))
		print("Lenght of Spades Deck: ", len(self.listSpades))


	def display_Length_of_Spare(self):
		#set of collection of how many cards have the sparre deck of the game
		print("Lenght of main Deck: ", len(self.listControl))
		i0 = 0
		while i0<7:
			print("Lenght of Spare Deck " , i0, ": ", len(self.listSpare[i0]))
			i0+=1
   


	def move_to(self, list_to, list_where, to_add):
		#move card from list_to to the list_where
		#final step on moving two cards
		kk = self.obtaincard(to_add)
		#print("=============Move To")
		#print("Number is: ", kk.ret_number())
		#print("Type is: ", kk.ret_type())
		#print("Color is: ", kk.ret_color())
		if to_add in list_to:
			list_to.remove(to_add)
			list_where.insert(len(list_where),to_add)
			return True
		return False

	def to_Insert_Unorganize_long_section(self, spare_num_from, spare_num_to, started_from_spare):
		# Only work with two spare lists
		# spare_num_from => where we are moving the elements from
		# spare_num_to => where we are inserting
		# started_from_spare => where the seectionof card moving from the spare deck
		#print("To insert a list on unorganize spare")
		if self.check_list_Unorganize(spare_num_from, started_from_spare):
			#print("List coming from is organize")
			i0 = len(self.listSpare[spare_num_from])
			lenX = i0 -started_from_spare
			print("NUMBER OF CARDS TO MOVE: ", lenX)
			if self.to_Insert_Unorganize(self.listSpare[spare_num_from][started_from_spare], spare_num_to, spare_num_from):
				#print("\t move item from list happen")
				print("\tThis happen")
				i0=1
				while i0 < lenX:
					if self.to_Insert_Unorganize(self.listSpare[spare_num_from][started_from_spare], spare_num_to, spare_num_from):
						print("\tThis happen")
						# print("\tNo problem happening on operation")
						# return True
					else:
						#print("GRAVE EROR HAPPENING")
						return False
					i0+=1
    			
				return True
			else:
				#print("Value can not be inserted")
				return False
		else:
			#print("ERROR, the list coming froom is not organize")
			return False


	def check_list_Unorganize(self, spare_num, run_W):
		# check if part of deeteermine list of spare deck follow unorgnize patron
		# spare_num is the number of the spare list using
		# run_W is the number from where the list will run from to zero
		#print("check list")
		lenX = len(self.listSpare[spare_num])
		if spare_num > 7:
			return False
			# it is not a number of spare  listt
		if run_W == lenX-1:
			#print("\t No need of unorganize check")
			return True
		elif run_W >= lenX:
			#print("WRONG NUMBER OPTIONAL")
			return False
		if run_W < lenX-1:
			i2 = run_W
			card_c = self.deckA.ret_card(self.listSpare[spare_num][i2])
			color0 = card_c.ret_color()
			number0 = card_c.ret_number()
			i2+=1
			while i2 < lenX:
				card_c = self.deckA.ret_card(self.listSpare[spare_num][i2])
				color1 = card_c.ret_color()
				number1 = card_c.ret_number()
				#print("\t TO COMPARE IS: " , color0, " + ", number0 ,  " => ", color1, " + ", number1)
				if color0 == color1 and number0 != number1+1:
					return False
				color0 = color1
				number0 = number1
				# card_c.description()
				# print("\n")
				i2+=1
		return True

	def to_Insert_Contol(self, place_to_add, where_come_from):
		# action set up in case you wish to move card into respective organize same symbol column
		# place_to_add mean the symbol of card to allocate
		# to_add: id of card wishing to add 
		# where_come_from: it is a number that represent the list to select 0-7 mean a sparree list; 8 mean listcontrol
		if place_to_add == "Spare":
			if self.to_Insert_Unorganize(self.listControl[self.setcount[0]-1], where_come_from, 8): #the 8 at the endd it is refeering to listControl where the value is coming from
				self.setcount[0] =  self.setcount[0]-1
				return True
		else:
			if self.to_Insert(self.listControl[self.setcount[0]-1], place_to_add, where_come_from):
				self.setcount[0] = self.setcount[0]-1
				return True
		return False
	
	def to_Insert(self, to_add, place_to_add, where_come_from):
		# action set up in case you wish to move card into respective organize same symbol column
		# place_to_add meean the symbol of card to allocate
		# to_add: id of card wishing to add 
		# where_come_from: it is a number that represent the list to select 0-7 mean a sparree list; 8 mean listcontrol
		#print("To Insert: ")
		if place_to_add == "Heart":
			#print("On Deck")
			if self.compareList("Heart", to_add):
				#print("\t\t\tInsert element on List")
				return self.where_to_move( self.listHeart, where_come_from , to_add)
			else:
				#print("\t\t\tCard fail on Insert")
				return False		
		elif place_to_add == "Clover":
			#print("On Deck")
			if self.compareList("Clover", to_add):
				#print("\t\t\tInsert element on List")
				return self.where_to_move( self.listClover, where_come_from ,to_add)
			else:
				#print("\t\t\tCard fail on Insert")
				return False
		elif place_to_add == "Diamond":
			# print("On Deck")
			if self.compareList("Diamond", to_add):
				#print("\t\t\tInsert element on List")
				return self.where_to_move( self.listDiamond, where_come_from, to_add)
			else:
				#print("\t\t\tCard fail on Insert")
				return False
		elif place_to_add == "Spades":
			# print("On Deck")
			if self.compareList("Spades", to_add):
				#print("\t\t\tInsert element on List")
				return self.where_to_move( self.listSpades, where_come_from ,to_add)
			else:
				#print("\t\t\tCard fail on Insert")
				return False
		return False

	def where_to_move(self, where_to_add, where_come_from, to_add):
	# method to verify where we are moving element to which list;
	# considering both if spare list or symbol list
	#  where_to_add is a List
		if where_come_from == 8:
			return self.move_to( self.listControl, where_to_add, to_add)
		elif where_come_from == 9:
			return self.move_to( self.listHeart, where_to_add , to_add)
		elif where_come_from == 10:
			return self.move_to( self.listClover, where_to_add, to_add)
		elif where_come_from == 11:
			return self.move_to( self.listSpades, where_to_add, to_add)
		elif where_come_from == 12:
			return self.move_to( self.listDiamond, where_to_add, to_add)
		elif where_come_from <= 7 and where_come_from >=0:
			return self.move_to( self.listSpare[where_come_from], where_to_add, to_add)


	def compareList(self, type_list, to_add):
		#to_add = ID of card to insert
		#typee_list: type of card whereto insert
		card_type = self.deckA.ret_card_type(to_add)
		# print("\t\t\t This is a sudden change: ", card_type)
		if type_list == "Heart" and card_type == "Heart":
			#print("For List of Heart")
			return self.if_Insert(self.listHeart, to_add)
		elif type_list == "Clover" and card_type == "Clover":
			#print("For List of Clover")
			return self.if_Insert(self.listClover, to_add)
		elif type_list == "Diamond" and card_type == "Diamond":
			#print("For List of Diamond") 
			return self.if_Insert(self.listDiamond, to_add)
		elif type_list == "Spades" and card_type == "Spades":
			#print("For List of Spades")
			return self.if_Insert(self.listSpades, to_add)
		return False

	def if_Insert(self, list_W, to_add):
		#Organize list from smaller to bigger numbers with the same symbol
		#list_W is thee list where we are adding card
		if len(list_W) == 0:
			#print("\tList  is Empty")
			kk = self.deckA.ret_card(to_add)
			if kk.ret_value() == "ACE":
				#print("\t\tThis is an ACE")
				return True
		elif len(list_W) == 13:
			#print("\tList is Full")
			return False
		else:
			#print("\tList is Incomplete")
			kk = self.deckA.ret_card(to_add)
			# kk2 = self.deckA.ret_card(len(list_W)-1)
			kk2 = self.deckA.ret_card(list_W[len(list_W)-1])
			if kk2.ret_number() == kk.ret_number()-1:
				#print("\t\tSequence Work ", kk2.ret_number(), " and ", kk.ret_number() )
				return True
		return False
		#print("Type: ", kk)

	def to_Insert_Unorganize(self, to_add, spareL_to_add, where_from_L):
		# to_add is the card id
		#spareL_to_add =>number of the list Spare inserting into
		#where_from_L =>  number too refer to the list where the element is coming from
		#print("To Insert: ")
		if spareL_to_add < 7:
			#print("On Deck")
			if self.if_Insert_UnOrganize(self.listSpare[spareL_to_add], to_add):
				#print("\t\t\tInsert element on List")
				# return self.move_to( where_from_L, self.listSpare[spareL_to_add], to_add)
				return self.where_to_move(self.listSpare[spareL_to_add], where_from_L, to_add)
			else:
					#print("\t\t\tCard fail on Insert")
					return False
		# else:			
		# 	print("\t\t\t This number is worng")

	def if_Insert_UnOrganize(self, list_W, to_add):
		#Organize list from smaller to bigger numbers with opposite Color
		# print("<><><><><><><><><<>><><><><><><><><><<><><><><>")
		# self.displayDeck_Spare(1)
		# print("<><><><><><><><><<>><><><><><><><><><<><><><><>")
		# print("\t", list_W)
		#print("\t id", to_add)
		if len(list_W) == 0:
			#print("\tList  is Empty")
			kk = self.deckA.ret_card(to_add)
			if kk.ret_value() == "KING":
				#print("\t\tThis is an KING")
				return True
		elif len(list_W) == 13:
			#print("\tList is Full")
			return False
		else:
			#print("\tList is Incomplete")
			kk = self.deckA.ret_card(to_add)
			#print("\kk = ", kk)
			kk2 = self.deckA.ret_card(list_W[len(list_W)-1])

			# print("\t======== ID= ",to_add)
			# print("\t1-type: ", kk.ret_type())
			# print("\t1-number: ", kk.ret_number())
			# print("\t1-color: ", kk.ret_color())
			# print("\t======== ID= ", list_W[len(list_W)-1])
			# print("\t2-type: ", kk2.ret_type())
			# print("\t2-number: ", kk2.ret_number())
			# print("\t2-color: ", kk2.ret_color())

			# if kk2.ret_number() == kk.ret_number()-1:
			if kk2.ret_number() == kk.ret_number()+1:
				#print("\t\tSequence Work ", kk2.ret_number(), " and ", kk.ret_number() )
				if kk2.ret_color() != kk.ret_color():
					#print("\t\t\tColor Sequence Work ", kk2.ret_color(), " and ", kk.ret_color() )
					return True
		return False
		#print("Type: ", kk)

	def obtaincard(self, id):
		return self.deckA.ret_card(id)

	def obtainid_top_collection(self, collection_name):
    	#return card from the top collection of respective name
		if collection_name == "Heart":
			if len(self.listHeart) >0:
				return self.listHeart[len(self.listHeart)-1]
		elif collection_name == "Clover":
			if len(self.listClover) >0:
				return self.listClover[len(self.listClover)-1]
		elif collection_name == "Diamond":
			if len(self.listDiamond) >0:
				return self.listDiamond[len(self.listDiamond)-1]
		elif collection_name == "Pica":
			if len(self.listSpades) >0:
				return self.listSpades[len(self.listSpades)-1]

	def shuffle_Control(self):
		random.shuffle(self.listControl)

	def set_control(self):
	#list control+. return the top three card on the list Control
		# self.setcount = self.setcount+3
		#print("Print set count:  ", self.setcount[0], end="")
		if len(self.listControl) >= self.setcount[0] +3:
			self.setcount[0] = self.setcount[0]+3
			#print(" => ", self.setcount[0])
			#print("\tTHIS IS CONTROL")
		elif len(self.listControl) >= self.setcount[0]+2:
			self.setcount[0] = self.setcount[0]+2
			#print(" => ", self.setcount[0])
			#print("\tTHIS IS CONTROL")
		elif len(self.listControl) >= self.setcount[0]+1:
			self.setcount[0] = self.setcount[0]+1
			#print(" => ", self.setcount[0])
			#print("\tTHIS IS CONTROL")
		else:
			self.setcount[0] = 0
			#print(" => ", self.setcount[0])
			#print("\tAbove limit => ",self.setcount[0])
  		
			
		# return self.listControl
	def set_card(self):
		#print thee number of cards of list control that should be displayed considering the setcount[0] variable
		ix = self.setcount[0]
		if ix < 3:
			listK = self.listControl[:self.setcount[0]]
			# print("\tPrint CardX: ", listK)
			return listK
		listK = self.listControl[self.setcount[0]-3:self.setcount[0]]
		# print("\tPrint Card: ", listK)
		return listK

	def set_card_last(self):
		#return the last id card that shold be presented on the list
		cardK = self.listControl[self.setcount[0]-1]
		# print("\tPrint Card: ", listK)
		return cardK

