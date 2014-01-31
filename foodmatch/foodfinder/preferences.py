class Preferences(object):
	"""A user's preferred menu items/location/times"""

	def __init__(self, names=[], locations=[], times=[]):
		self.names = names
		self.locations = locations
		self.times = times

	@classmethod
	def createFromString(cls, preferences):
		"""Creates preferences from a String of the form: name1, name2 : location1, location2 : time1, time2"""
		preferences = preferences.replace(" ", "")
		preferences = preferences.split(':')
		names = preferences[0].split(',')
		locations = preferences[1].split(',')
		times = preferences[2].split(',')
		return cls(names, locations, times)

	def add_item_name(self, name):
		self.names.append(name)

	def add_location(self, location):
		self.locations.append(location)

	def add_times(self, time):
		self.times.append(time)

	def get_names(self):
		return self.names

	def get_locations(self):
		return self.locations

	def get_times(self):
		return self.times