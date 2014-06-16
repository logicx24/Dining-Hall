import os
from menu import Menu
from food import Food
#from django import conf.settings

class MenuParser(object):
	#menu_path = os.path.join(settings.PROJECT_ROOT, 'menu.txt')
	menu_path = "menu.txt"

	def __init__(self, path=menu_path):
		menu_file = open(path)
		self.menu = str(menu_file.read())
		menu_file.close()
		self.is_parsed = False

	def parse_menu(self):
		if self.is_parsed:
			return self.menu
		#self.diner = self.diner.lower()
		#self.diner = self.diner.splitlines()
		self.menu = self.menu.splitlines()
		parsed_menu = Menu()
		for menu_item in self.menu:
			menu_item = menu_item[1:-1] # remove parenthases
			menu_item = menu_item.split(',')
			menu_item = Food(menu_item[0], menu_item[1], menu_item[2])
			parsed_menu.add_item(menu_item)
		self.is_parsed = True
		self.menu = parsed_menu
		return self.menu

#menu = MenuParser("/Users/kklin/development/Dining-Hall/foodmatch/foodmatch/menu.txt")
