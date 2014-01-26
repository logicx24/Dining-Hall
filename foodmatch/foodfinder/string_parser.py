class StringRectifier(object):

	def __init__(self, string):
		self.corpus = string
		self.diner = initialize_txt()
		#self.diner1 = initialize_txt()
		#self.corpus1 = string[:]
		self.meals = {1:'Breakfast', 2:'Lunch/Brunch', 3:'Dinner'}
		self.halls = {1: 'Crossroads', 2:'Unit 3', 3:'Foothill', 4:'Clark Kerr'}

	def remove_crap(self):
		self.corpus = self.corpus.lower()
		#self.corpus1 = self.corpus1.lower() #Duplicate corpus
		self.corpus = [self.corpus.strip() for self.corpus in self.corpus.split(',')] #Split by comma
		#self.corpus1 = self.corpus1.split() #Split by word
		#return self.corpus
		#print(self.corpus, self.corpus1)

	def matching(self):
		x, x1 = {}, {}
		y = ['breakfast','lunch','dinner','brunch','crossroads','unit 3 cafe', 'foothill','clark kerr commons']
		z, z1 = {}, {}
		a, a1 = [], []
		self.diner = self.diner.lower()
		self.diner = self.diner.splitlines() #Split by phrase
		#self.diner1 = self.diner1.split() #Split by word
		self.diner = [r.strip(' ') for r in self.diner]
		hall, hall1 = 1,1
		meal,meal1 = 1,1

		for element in self.diner: #Assemble dictionary by name
			if element == '<-->':
				meal+= 1
			if element == '<->':
				meal = 1
			if element == '<--->':
				hall += 1
			else:
				x[element] = [meal, hall]

		for element in x:
			for element2 in self.corpus:
				if element2 in element:
					z[element] = x[element]

		for element in z:
			a.append([element]+z[element])


		for element in a:
			element[1] = self.meals[element[1]]
			element[2] = self.halls[element[2]]

		return a

def initialize_txt():
	file1 = open("sample_menu.txt")
	data = file1.read()
	str1 = str(data)
	file1.close()
	return str1
