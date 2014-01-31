class Menu(object):

	def __init__(self):
		self.items = []

	def add_item(self, food):
		self.items.append(food)

	def match_name_with(self, preferences):
		preferences = preferences.split(',')
		preferences = [preference.replace(" ", "") for preference in preferences]
		item_names = [item.name for item in self.items]
		matches = []
		for preference in preferences:
			for i, item_name in enumerate(item_names): 
				if preference in item_name:
					matches.append(self.items[i]) # TODO: append food object, not name
		return matches

	def __repr__(self):
		return self.items.__repr__()