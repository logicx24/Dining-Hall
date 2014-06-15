from bs4 import BeautifulSoup, Comment
from foodfinder.food import Food
import urllib2
import datetime

#"populate_day mostly created by https://github.com/mikehcheng"
#python 2.75
#html5lib is requried, pip install html5lib

def scrape_menus():

    response = urllib2.urlopen('http://services.housing.berkeley.edu/FoodPro/dining/static/todaysentrees.asp')
    html = response.read()

    #trash.py - go for <!-- -->
    content = BeautifulSoup(html, 'html5lib').find_all(id = 'content')[2].tbody.find_all(
        'tr', {"valign":"top"})

    LOCATIONS = {0: "crossroads", 1: "cafe_3", 2: "foothill", 3: "clark_kerr"}
    #FOODTYPE = {u'#800040': 'Vegan', u'#008000': 'Vegetarian', u'#000000': 'Regular'}
    #more than one vegetarian color o__O

    all_food = []

    for time in content: #b/l/d
        for l, loc in enumerate(time.find_all('td')): #cr/c3/fh/ck
            meal = unicode(loc.find('b').string) #meals bolded
            #TRASH.PY
            if meal == u"Lunch/Brunch": 
                meal = u"Lunch"
            entrees = loc.find_all('a')      #all meals linked to nutrition
            for entree in entrees:
                name = unicode(entree.string)
                #ftype = FOODTYPE[unicode(entree.font['color'])]
                dininghall = LOCATIONS[l]
                name = str(name)

                all_food.append(Food(name, dininghall, meal))

    return all_food

if __name__ == "__main__":
    all_food = scrape_menus()
    file = open('foodmatch/menu.txt', 'w')
    cumulative = open('cumulative_menu.txt', 'a')
    cumulative.write("===================================\n")
    cumulative.write(str(datetime.datetime.now()).split('.')[0] + "\n")
    for food in all_food:
        file.write( "(" + str(food.name) + "," + str(food.location) + "," + str(food.meal) + ")")
        file.write("\n")
        cumulative.write( "(" + str(food.name) + "," + str(food.location) + "," + str(food.meal) + ")")
        cumulative.write("\n")
    file.close()

