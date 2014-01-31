from twilio.rest import TwilioRestClient
from menu_parser import MenuParser

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodmatch.settings')
from foodfinder.models import UserProfile, User

account_sid = "AC20e35fdf8d24f77f436bf74f8bf18448"
auth_token  = "2888edea88ebe1402dc28e2b5f404981"
client = TwilioRestClient(account_sid, auth_token)

menu_path = os.path.join(conf.settings.PROJECT_ROOT, 'menu.txt')
menu = MenuParser(menu_path)
menu = menu.parse_menu()

user = User.objects.get(username="test")
user_profile = UserProfile.objects.get(user=user)
preferences = user_profile.preferences
preferences = Preferences.createFromString(preferences)
matches = menu.match_with(preferences)
body = ""
for item in matches.get_items(): # TODO: make menu object iterable
	body += item.name + " is available\n"
	
client.messages.create(body=body, to='+18312240500',from_="+18319204557")