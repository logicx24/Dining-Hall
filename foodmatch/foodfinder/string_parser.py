import os

class StringRectifier(object):

	def __init__(self, string, file1):
		self.file1 = file1
		self.corpus = string
		self.diner = self.initialize_txt()
		self.meals = {1:'Breakfast', 2:'Lunch/Brunch', 3:'Dinner'}
		self.halls = {1:'Crossroads', 2:'Unit 3', 3:'Foothill', 4:'Clark Kerr'}

	def initialize_txt(self):
		path = "Users/aakashjapi/Dropbox/Dining-Hall/foodmatchdfinder/menu.txt"
		data = self.file1.read()
		str1 = str(data)
		#self.file1.close()
		return str1

	def remove_crap(self):
		self.corpus = self.corpus.lower()
		self.corpus = [self.corpus.strip() for self.corpus in self.corpus.split(',')] #Split by comma

	def matches(self):
		self.diner = self.diner.lower()
		self.diner = self.diner.splitlines()

		for i,el in enumerate(self.diner):
			x,y=[],[]
			for index in range(len(el)):
				if el[index] != '(' and el[index] != ')':
					x.append(el[index])
					if el[index] == ',':
						joined = ''.join(x)
						x=[]
						y.append(joined)
				if el[index] == ')':
					y.append(''.join(x))
					self.diner[i] = y

		z = []
		for element in self.diner:
			for element2 in self.corpus:
				if element2 in element[0]:
					z.append(element)

		r = 0

		for element in z:
			for r in range(len(element)): 
				#if r >= 1:
				#	if (element[r-1] in element[r]) or (element[r] in element[r-1]):
				#		element.pop(r)
				element[r] = element[r].strip(',')
		return z