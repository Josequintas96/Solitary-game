from deck_logic import *

class Record():
	record_h = 0
	record_setcount = [] #variable to manage the three cards present in front
	record_listControl = [] #deck at hand
	record_listClover = [] #accumulation of clover cards
	record_listDiamond = [] #accumulation of Diamond cards
	record_listSpades = [] #accumulation of Spades cards
	record_listHeart = [] #accumulation of Heart cards
 
	record_listSpare = []
	record_listflipSpare=[]
 
	
	def __init__(self):
		self.record_h = 0
  
	def print_record_length(self):
		print("\tLenght of record control: ", len(self.record_listControl))
		print("\tLenght of record Heart: ", len(self.record_listHeart))
		print("\tLenght of record Diamond: ", len(self.record_listDiamond))
		print("\tLenght of record Clover: ", len(self.record_listClover))
		print("\tLenght of record Spade: ", len(self.record_listSpades))
		print("\tLenght of record Spares: ", len(self.record_listSpare))
  
	def print_record(self):
		print("Lenght of record: ", self.record_h)
		print("\tRecord control: ", self.record_listControl[self.record_h-1])
		print("\tRecord Heart: ", self.record_listHeart[self.record_h-1])
		print("\tRecord Diamond: ", self.record_listDiamond[self.record_h-1])
		print("\tRecord Clover: ", self.record_listClover[self.record_h-1])
		print("\tRecord Spade: ", self.record_listSpades[self.record_h-1])
		print("\tRecord Spares: ", self.record_listSpare[self.record_h-1])
		print("\tRecord State Spares: ", self.record_listflipSpare[self.record_h-1])

	def pop_record(self):
		self.record_listControl.pop()
		self.record_listClover.pop()
		self.record_listDiamond.pop()
		self.record_listSpades.pop()
		self.record_listHeart.pop()
		self.record_listSpare.pop()
		self.record_listflipSpare.pop()
		self.record_setcount.pop()
		self.record_h -=1

	def set_record(self, deck, list_control, list_clover, list_heart, list_spades, list_diamond, list_spare, list_count):
		self.set_record_Control(list_control)
		self.set_record_Clover(list_clover)
		self.set_record_Heart(list_heart)
		self.set_record_Spades(list_spades)
		self.set_record_Diamond(list_diamond)
		self.set_record_Spare(deck, list_spare)
		self.record_setcount.append(list_count[0])
		self.record_h +=1


	def set_record_Control(self, list_control):
		#print("save record control")
		record_l = []
		i0 = 0
		iX = len(list_control)
		while i0 < iX:
			li = list_control[i0]
			record_l.append(li)
			i0+=1
		self.record_listControl.append(record_l)
		
	def set_record_Clover(self, list_clover):
		#print("save record clover")
		record_l = []
		i0 = 0
		iX = len(list_clover)
		while i0< iX:
			li = list_clover[i0]
			record_l.append(li)
			i0+=1
		self.record_listClover.append(record_l)
		
	def set_record_Heart(self, list_heart):
		#print("save record clover")
		record_l = []
		i0 = 0
		iX = len(list_heart)
		while i0< iX:
			li = list_heart[i0]
			record_l.append(li)
			i0+=1
		self.record_listHeart.append(record_l)
		
	def set_record_Spades(self, list_spades):
		#print("save record spades")
		record_l = []
		i0 = 0
		iX = len(list_spades)
		while i0< iX:
			li = list_spades[i0]
			record_l.append(li)
			i0+=1
		self.record_listSpades.append(record_l)
		

	def set_record_Diamond(self, list_diamond):
		#print("save record diamond")
		record_l = []
		i0 = 0
		iX = len(list_diamond)
		while i0< iX:
			li = list_diamond[i0]
			record_l.append(li)
			i0+=1
		self.record_listDiamond.append(record_l)

	def set_record_Diamond(self, list_diamond):
		#print("save record diamond")
		record_l = []
		i0 = 0
		iX = len(list_diamond)
		while i0< iX:
			li = list_diamond[i0]
			record_l.append(li)
			i0+=1
		self.record_listDiamond.append(record_l)
  
	def set_record_Spare(self, deck, list_spare):
		#print("save record spare")
		record_l = [] #SAVE NUMBER FROMLIST
		record_S = [] #Save state from card
		i0 = 0
		iX = len(list_spare)
		while i0< iX:
			i1 = 0
			record_l2 = []
			record_S2 = []
			lenX2 = len(list_spare[i0])
			# print("\t\t Set len is ", lenX2)
			while i1 < lenX2:
				li = list_spare[i0][i1]
				si = deck.deckZ[li].ret_state()
				#print("\t\t State of cards: ", si)
				record_l2.append(li)
				record_S2.append(si)
				i1+=1
			record_l.append(record_l2)
			record_S.append(record_S2)
			i0+=1
		self.record_listSpare.append(record_l)
		self.record_listflipSpare.append(record_S)
  
	def restort_record(self, deck, list_control, list_clover, list_heart, list_spades, list_diamond, list_spare, list_count):
		if self.record_h-2>=0:
			self.restort_record_Control(list_control, self.record_h-2)
			self.restort_record_Clover(list_clover, self.record_h-2)
			self.restort_record_Heart(list_heart, self.record_h-2)
			self.restort_record_Spade(list_spades, self.record_h-2)
			self.restort_record_Diamond(list_diamond, self.record_h-2)
			self.restort_record_Spare(list_spare, self.record_h-2)
			self.restort_record_flip(deck, self.record_h-2)
			self.restort_list_count(list_count, self.record_h-2)
			self.pop_record()
		else:
			print("NO UNDO")


	def restort_record_Control(self, list_control, record):
		#print("restort record control")
		i0 = 0
		#print("\tLength of listControl record: ", len(self.record_listControl) )
		#print("\t Record: ", record )
		iX = len(self.record_listControl[record])
		iX2 = len(list_control)
		while i0< iX:
			if i0 < iX2:
				if self.record_listControl[record][i0] != list_control[i0]:
					list_control.insert(i0, self.record_listControl[record][i0] )
			else:
				list_control.append(self.record_listControl[record][i0])
			i0+=1

	def restort_record_Clover(self, list_clover, record):
		#print("restort record Clover => ", list_clover)
		i0 = 0
		iX = len(self.record_listClover[record])
		iX2 = len(list_clover)
		if iX < iX2:
			iX3 = iX2-iX
			while i0 < iX3:
				list_clover.pop()
				i0+=1
		else:
			while i0< iX:
				if i0 < iX2:
					if self.record_listClover[record][i0] != list_clover[i0]:
						list_clover.insert(i0, self.record_listClover[record][i0] )
				else:
					list_clover.append(self.record_listClover[record][i0])
				i0+=1
		#print("END restort record Clover => ", list_clover)

	def restort_record_Heart(self, list_heart, record):
		#print("restort record Heart")
		i0 = 0
		iX = len(self.record_listHeart[record])
		iX2 = len(list_heart)
		if iX < iX2:
			iX3 = iX2-iX
			while i0 < iX3:
				list_heart.pop()
				i0+=1
		else:
			while i0< iX:
				if i0 < iX2:
					if self.record_listHeart[record][i0] != list_heart[i0]:
						list_heart.insert(i0, self.record_listHeart[record][i0] )
				else:
					list_heart.append(self.record_listHeart[record][i0])
				i0+=1

	def restort_record_Spade(self, list_spades, record):
		#print("restort record Spade")
		i0 = 0
		iX = len(self.record_listSpades[record])
		iX2 = len(list_spades)
		if iX < iX2:
			iX3 = iX2-iX
			while i0 < iX3:
				list_spades.pop()
				i0+=1
		else:
			while i0< iX:
				if i0 < iX2:
					if self.record_listSpades[record][i0] != list_spades[i0]:
						list_spades.insert(i0, self.record_listSpades[record][i0] )
				else:
					list_spades.append(self.record_listSpades[record][i0])
				i0+=1
   
	def restort_record_Diamond(self, list_diamond, record):
		#print("restort record Spade")
		i0 = 0
		iX = len(self.record_listDiamond[record])
		iX2 = len(list_diamond)
		if iX < iX2:
			iX3 = iX2-iX
			while i0 < iX3:
				list_diamond.pop()
				i0+=1
		else:
			while i0< iX:
				if i0 < iX2:
					if self.record_listDiamond[record][i0] != list_diamond[i0]:
						list_diamond.insert(i0, self.record_listDiamond[record][i0] )
				else:
					list_diamond.append(self.record_listDiamond[record][i0])
				i0+=1

	def restort_record_Spare(self, list_spare, record):
		#print("COMPARING: ",self.record_listSpare[record] )
		#print("BGN restort record Spare, ", list_spare)
		i00 = 0
		iX0 = len(self.record_listSpare[record])
		while i00 < iX0:
			i0 = 0
			# print("Mysterious value: ",self.record_listSpare[record][i00])
			iX = len(self.record_listSpare[record][i00])
			iX2 = len(list_spare[i00])
			if iX < iX2:
				iX3 = iX2-iX
				while i0 < iX3:
					#print("\tDDOES THIS HAPPEN")
					list_spare[i00].pop()
					i0+=1
			else:
				while i0< iX:
					if i0 < iX2:
						if self.record_listSpare[record][i00][i0] != list_spare[i00][i0]:
							#print("UNEQUAL INSERTION => ", self.record_listSpare[record][i00][i0])
							list_spare[i00].insert(i0, self.record_listSpare[record][i00][i0] )
					else:
						list_spare[i00].append(self.record_listSpare[record][i00][i0])
						#print("\ttTHIS SHOUULD BE APPENDED: ", self.record_listSpare[record][i00][i0])
					i0+=1
			i00+=1
		#print("END restort record Spare, ", list_spare)

	def restort_record_flip(self, deck, record):
		# print("List FLIP: ", self.record_listflipSpare[record] )
		i00 = 0
		iX0 = len(self.record_listSpare[record])
		while i00 < iX0:
			i0 = 0
			# print("Mysterious value: ",self.record_listSpare[record][i00])
			iX = len(self.record_listSpare[record][i00])
			while i0< iX:
				card_undo = self.record_listSpare[record][i00][i0]
				if i0 < iX:
					# print("This is card: ",deck.deckZ[card_undo].ret_state(), " and this is state of card ",self.record_listflipSpare[record][i00][i0]  )
					if deck.deckZ[card_undo].ret_state() != self.record_listflipSpare[record][i00][i0]:
						# print("\t\t ARE NOT FLIP ACCORDINGLY")
						if self.record_listflipSpare[record][i00][i0] == "hidden":
							deck.deckZ[card_undo].flip_back()
						elif self.record_listflipSpare[record][i00][i0] == "reveal":
							deck.deckZ[card_undo].flip_card()
				i0+=1
			i00+=1

	def restort_list_count(self, list_count, record):
		list_count[0] = self.record_setcount[record]



