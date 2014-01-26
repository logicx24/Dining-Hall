

from django.core.management import setup_environ
from foodmatch import settings
from twilio.rest import TwilioRestClient
from foodfinder.models import User, UserProfile
from string_parser import StringRectifier

setup_environ(settings)

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACeb7c885bc8076ac960a2a1e8f06de1aa"
auth_token  = "1c70dd1e8a76c953b561845665ced631"
client = TwilioRestClient(account_sid, auth_token)
 
all_users = User.objects.all()

for person in all_users: 
	profile = UserProfile.objects.get(user=user)
	matches = get_matches(person, profile)
	if matches != "":
		message = client.messages.create(body="",
	    	to='+19175867213',
	    	from_="+17184739056")
		print message.sid


def get_matches(user, profile):
	x = StringRectifier(profile.preferences)
	x.remove_crap()
	matches = x.matching()
	message = ""
	meals = ['breakfast','lunch','dinner']
	hall = ["crossroads", "cafe 3", "foothill", "clark kerr"]
	for match in matches:
		message += "We found a match! "+match[0]+" is being served during "+meals[match[1]-1]+" at "+hall[match[2]-1]+". "
	return message

