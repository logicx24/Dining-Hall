from twilio.rest import TwilioRestClient
from foodfinder.menu_parser import MenuParser
from foodfinder.preferences import Preferences
from django.conf import settings

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodmatch.settings')
from foodfinder.models import UserProfile, User

account_sid = "AC20e35fdf8d24f77f436bf74f8bf18448"
auth_token  = "2888edea88ebe1402dc28e2b5f404981"
client = TwilioRestClient(account_sid, auth_token)

menu_path = os.path.join(settings.PROJECT_ROOT, 'menu.txt')
menu = MenuParser(menu_path)
menu = menu.parse_menu()

for user_profile in UserProfile.objects.all():
	preferences = user_profile.preferences
	preferences = Preferences.createFromString(preferences)
	matches = menu.match_with(preferences)
	body = ""
	for item in matches.get_items(): # TODO: make menu object iterable
		body += item.name + " at " + item.location + " for " + item.meal + "\n"
	
	if body != "":
		print("sent following to " + str(user_profile.phone) + ":\n" + body)
		client.messages.create(body=body, to=str(user_profile.phone),from_="+18319204557")