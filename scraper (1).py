from bs4 import BeautifulSoup
import requests



BASE_URL = 'http://services.housing.berkeley.edu/FoodPro/dining/static/'
MENU_URL = 'todaysentrees.asp'
MEALS = {'breakfast':3, 'lunch': 5}
DINING_COMMONS = {'crossroads':1, 'cafe3': 3, 'foothill': 5}
VEGE_LEGEND = {'vegan':'#800040', 'vegetarian':'#008000'}

class food_obj(object):
    def __init__(self, meal, dc, item):
      self.item = item
      self.dc = dc
      self.meal = meal
def http_get(url):
  resp = requests.get(url)
  return BeautifulSoup(resp.text, "lxml")

def crawl():
  # make web request
  soup = http_get(BASE_URL + MENU_URL)
  # locate html data
  html = soup.body.contents[1].table.tbody.contents[3].td.table.contents

  # stores food that has already been added to the table
  food_cache = {}

  # extract data
  for MEAL in MEALS:
    meal_index = MEALS[MEAL]
    meal_data = html[meal_index]

    for DINING_COMMON in DINING_COMMONS:
      dc_index = DINING_COMMONS[DINING_COMMON]
      meal_dc_data = meal_data.contents[dc_index]

      for entry in meal_dc_data.find_all('a'):
        meal_name = entry.contents[0].string
        meal_name, gluten_free = truncate_meal_name(meal_name)

        # skip the "Nutritive Analysis" link
        if 'nutritive analysis' in meal_name.lower():
          continue

        # create database models object
        #if meal_name in food_cache:  
          #food_obj = food_cache[meal_name]
        #else:
            # add food to the cache
        food_cache[meal_name] = food_obj(MEAL,DINING_COMMON, meal_name)
  
  file = open('out.txt', 'w')
  for key in food_cache.keys():
    file.write( "(" + str(food_cache[key].item) + "," + str(food_cache[key].dc) \
                                                + "," + str(food_cache[key].meal) + ")")
    file.write("\n")
    
  file.close()
  

# truncate Honey Bear or Gluten Free prefix
#   returns pair of meal name, and if its gluten free or not
def truncate_meal_name(meal_name):
  gluten_free = False
  if meal_name[0:3] == 'HB ':
    meal_name = meal_name[3:]
  elif meal_name[0:3] == 'GF ':
    meal_name = meal_name[3:]
    gluten_free = True
  return meal_name, gluten_free
crawl()