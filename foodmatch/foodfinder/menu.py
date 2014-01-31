from food import Food

class Menu(object):

	def __init__(self):
		self.items = []

	def add_item(self, food):
		self.items.append(food)

	def match_name_with(self, preferred_item_names):
		item_names = [item.name.lower() for item in self.items]
		preferred_item_names = [item.lower() for item in preferred_item_names]
		matches = Menu()
		for preference in preferred_item_names:
			for i, item_name in enumerate(item_names): 
				if preference in item_name:
					matches.add_item(self.items[i])
		return matches

	def match_location_with(self, preferred_locations):
		item_locations = [item.location.lower() for item in self.items]
		preferred_locations = [item.lower() for item in preferred_locations]
		matches = Menu()
		for preference in preferred_locations:
			for i, item_location in enumerate(item_locations): 
				if preference == item_location:
					matches.add_item(self.items[i])
		return matches

	def match_time_with(self, preferred_times):
		item_times = [item.meal.lower() for item in self.items]
		preferred_times = [item.lower() for item in preferred_times]		
		matches = Menu()
		for preference in preferred_times:
			for i, item_time in enumerate(item_times): 
				if preference == item_time:
					matches.add_item(self.items[i])
		return matches

	def match_with(self, preference):
		return self.match_name_with(preference.get_names()).match_location_with(preference.get_locations()).match_time_with(preference.get_times())

	def get_items(self):
		return self.items

	def __repr__(self):
		return self.items.__repr__()