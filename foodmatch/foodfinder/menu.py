class Menu(object):

	def __init__(self):
		self.items = []

	def add_item(self, food):
		self.items.append(food)

	def __repr__(self):
		return self.items.__repr__()