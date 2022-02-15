import random

class Card:
	typeZ = ""
	number = 0
	value = ""
	Color = ""
	state = "" #hidden or reveal
	def __init__(self, typeX, numberX, ColorX):
		self.typeZ = typeX
		self.number = numberX
		self.valueKK(self.number)
		self.Color = ColorX
		self.state = "reveal"
	def description(self):
		print("Type: ", self.typeZ)
		print("Value: ", self.value)
		print("Color: ", self.Color)
		print("State: ", self.state)
	def ret_type(self):
		#print("\tTypeZ: ",self.typeZ)
		return self.typeZ
	def flip_card(self):
		self.state = "reveal"
	def flip_back(self):
		self.state = "hidden"
	def ret_number(self):
		return self.number
	def ret_color(self):
		return self.Color
	def ret_value(self):
		return self.value
	def ret_state(self):
		return self.state
	def valueKK(self, numberZ):
		if numberZ == 1:
			self.value = "ACE"
		elif numberZ == 2:
			self.value = "TWO"
		elif numberZ == 3:
			self.value = "THREE"
		elif numberZ == 4:
			self.value = "FOUR"
		elif numberZ == 5:
			self.value = "FIVE"	
		elif numberZ == 6:
			self.value = "SIX"
		elif numberZ == 7:
			self.value = "SEVEN"
		elif numberZ == 8:
			self.value = "EIGHT"
		elif numberZ == 9:
			self.value = "NINE"
		elif numberZ == 10:
			self.value = "TEN"
		elif numberZ == 11:
			self.value = "JACK"
		elif numberZ == 12:
			self.value = "QUEEN"
		elif numberZ == 13:
			self.value = "KING"

class Deck:
	deckZ = {}
	id = 0
	orderX =[]
	def __init__(self):
		self.setDeck("Clover", "BLACK")
		self.setDeck("Diamond", "RED")
		self.setDeck("Spades", "BLACK")
		self.setDeck("Heart", "RED")
		i2=1
		for i2 in range(0,(self.id)):
			self.orderX.append(i2)

	def share_deck(self, list_W):
		# tqake list and insert deck on list
		i=0
		for i in range(len(self.orderX)):
			list_W.append(self.orderX[i])

	def setDeck(self, typeX, ColorX):
		i=1
		for i in range(1,14):
			self.deckZ[self.id] = Card(typeX, i, ColorX)
			self.id = self.id + 1
		#self.deckZ[1] = Card(typeX, "ACE")
	def ret_id(self):
		print("ID: ", self.id)

	def shuffleDeck(self):
		random.shuffle(self.orderX)

	def displayStandDeck(self):
		i=1
		for i in range(0,self.id):
			self.deckZ[i].description()
	def displayOrder(self):
		print(self.orderX)
	def displayDeck(self):
		for i in self.orderX:
			#print(i)
			self.deckZ[i].description()

	def displayControlDeck(self, list_W):
		#print list given
		if len(list_W) <= 0:
			print("The List is empty")
			return None
		i=0
		print("================")
		for i in range(len(list_W)):
			self.deckZ[list_W[i]].description()
			print("================")
   
	def ret_card(self, i3):
		return self.deckZ[i3]
	def ret_card_type(self, i3):
		#print("Here displaycard_type")
		return self.deckZ[i3].ret_type()
	def ret_card_value(self, i3):
		return self.deckZ[i3].ret_value()
	def ret_card_number(self, i3):
		return self.deckZ[i3].ret_number()
	def ret_card_color(self, i3):
		return self.deckZ[i3].ret_color()


#play = Deck()
#play.ret_id()		
#play.displayStandDeck()
#play.displayOrder()
#play.shuffleDeck()
#play.displayOrder()
#play.displayDeck()

#choice = Card("Clover", "ACE")
#choice.description()


#dict = {"h": choice}
#print()
#dict['h'].description()


