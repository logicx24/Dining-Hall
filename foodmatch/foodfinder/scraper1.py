from bs4 import BeautifulSoup, Comment
import urllib2

#"populate_day mostly created by https://github.com/mikehcheng"
#python 2.75
#html5lib is requried, pip install html5lib

class MenuItem():
        def __init__(self, food, dc, meal):
            self.food = food
            self.dc = dc
            self.meal = meal
        def __str__(self):
            print self.food
            print self.dc
            print self.meal
            print ".............."
            return "\n"
all_food = []
def populate_day():


    response = urllib2.urlopen('http://services.housing.berkeley.edu/FoodPro/dining/static/todaysentrees.asp')
    html = response.read()

    #trash.py - go for <!-- -->
    content = BeautifulSoup(html, 'html5lib').find_all(id = 'content')[2].tbody.find_all(
        'tr', {"valign":"top"})

    LOCATIONS = {0: "crossroads", 1: "cafe_3", 2: "foothill", 3: "clark_kerr"}
    #FOODTYPE = {u'#800040': 'Vegan', u'#008000': 'Vegetarian', u'#000000': 'Regular'}
    #more than one vegetarian color o__O

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
                
                all_food.append(MenuItem(name, dininghall,meal))
populate_day()
file = open('menu.txt', 'w')
for i in all_food:
    file.write( "(" + str(i.food) + "," + str(i.dc) + "," + str(i.meal) + ")")
    file.write("\n")
file.close()

