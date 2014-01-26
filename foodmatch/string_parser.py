class StringRectifier(object):

	def __init__(self, string, parsing_text=None):
		self.corpus = string
		self.diner = parsing_text

	def remove_crap(self):
		self.corpus = self.corpus.split()
		for index in range(len(self.corpus)):
			if ',' in self.corpus[index]:
				for i in range(len(self.corpus[index])):
					if self.corpus[index][i] == ',' or self.corpus[index][i] == '.':
						self.corpus[index] = self.corpus[index][:-1]
		return self.corpus

	



			
r = 'pizza, chocolate, beans, enchiladas, tacos'