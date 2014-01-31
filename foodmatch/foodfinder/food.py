class Food(object):
	# TODO: enumerate dining locations and times

	def __init__(self, name, location, meal):
		self.name = name
		self.location = location
		self.meal = meal

	def __repr__(self):
		return self.name + " at " + self.location + " for " + self.meal