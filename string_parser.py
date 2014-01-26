class StringRectifier(object):

	def __init__(self, string, parsing_text=None):
		self.corpus = string
		self.diner = parsing_text
		self.diner = self.initialize_txt()


	def remove_crap(self):
		self.corpus = self.corpus.lower()
		self.corpus = [self.corpus.strip() for self.corpus in self.corpus.split(',')]
		return self.corpus

	def matching(self):
		x = {}
		y = ['breakfast','lunch','dinner','brunch','crossroads','unit 3 cafe', 'foothill','clark kerr commons']
		z = {}
		a = []
		self.diner = self.diner.lower()
		self.diner = self.diner.splitlines()
		self.diner = [x.strip(' ') for x in self.diner]
		hall = 1
		meal = 1

		for element in self.diner:
			if element == '<-->':
				meal+= 1
			if element == '<->':
				meal = 1
			if element == '<--->':
				hall += 1
			else:
				x[element] = (meal, hall)

		for element in x:
			if element in self.corpus:
				z[element] = x[element]

		for element in z:
			a.append((element,)+z[element])

		return a

	

	def initialize_txt(self):
		file1 = open("sample_menu.txt")
		data = file1.read()
		str1 = str(data)
		file1.close()
		return str1



			 

