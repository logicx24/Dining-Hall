# Create your views here.
import os
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from foodfinder.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from foodfinder.models import UserProfile
from django.contrib.auth.models import User
from django import conf
from django.views.decorators.csrf import csrf_protect
from menu_parser import MenuParser
from preferences import Preferences
from django.core.context_processors import csrf

# file_ = open(os.path.join(settings.PROJECT_ROOT, 'menu.txt'))

def redirection(request):
	context = RequestContext(request)
	return HttpResponseRedirect('/foodfinder/index/')

def index(request):
	context = RequestContext(request)
	preference_list = UserProfile.objects
	all_entries = preference_list.all()
	x = []
	for entry in all_entries:
		y = entry.preferences
	return render_to_response('foodfinder/index.html', {'preference':y}, context)

request_record = 0

def random(request):
	context = RequestContext(request)
	return render_to_response('foodfinder/untitled.html', context)

def register(request):
	print("GOT HERE BITCHES")
	global request_record
	request_record = request
	context = RequestContext(request)
	c = {}
	c.update(csrf(request))
	registered = False
	if request.method == 'POST':
		print("GOT THE POST MANNNNNNNNN")
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			print("The form was uber valid")
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			profile.phone = request.POST['phone']
			profile.save()
			registered = True
		else:
			print("Nah there were issues baby")
			print user_form.errors, profile_form.errors
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
	c['user_form'] = user_form
	c['profile_form'] = profile_form
	c['registered'] = registered
	return render_to_response('foodfinder/register.html', c,
            context)

def user_login(request):
	context = RequestContext(request)
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/foodfinder/home/')
			else:
				return HttpResponse('Your account was disabled. Bitch.')
		else:
			print "Invalid login details."
			return HttpResponse("Invalid login details supplied. Foiled you, wannabe hacker.")
	else:
		return render_to_response("foodfinder/login.html", {}, context)

def get_context_dict(request):
	u = User.objects.get(username=request.user)
	try:
		up = UserProfile.objects.get(user=u)
	except:
		up = None
	context_dict = {'user': u, 'userprofile': up}
	return context_dict;

@csrf_protect
@login_required
def home(request):
	context = RequestContext(request)
	context_dict = get_context_dict(request)

	menu_path = os.path.join(conf.settings.PROJECT_ROOT, 'menu.txt')
	menu = MenuParser(menu_path)
	menu = menu.parse_menu()
	preferences = context_dict['userprofile'].preferences
	preferences = Preferences.createFromString(preferences)
	matches = menu.match_with(preferences)
	html = ""
	for item in matches.get_items(): # TODO: make menu object iterable
		html += "<div style='margin-bottom: 4px; width: 400px; float left;'>"
		html += "<font style='text-decoration: underline;'>"+item.name+"</font><font color='black'> for "+item.meal+" @ "+item.location+"</font>"
		html += "</div>"
	context_dict['matches'] = html
	return render_to_response("foodfinder/home.html", context_dict, context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/foodfinder/')

@login_required
def settings(request):
	context = RequestContext(request)
	u = User.objects.get(username=request.user)
	try:
		up = UserProfile.objects.get(user=u)
	except:
		up = None
	context_dict = {'user': u, 'userprofile': up}
	if request.method == "POST":
		new_prefs = request.POST.get('preferences')
		up.preferences = new_prefs
		up.save()
		return HttpResponseRedirect('/foodfinder/home/')
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	#return render_to_response('foodfinder/settings.html', {'user_form': user_form, 'profile_form': profile_form}, context)
	return render_to_response("foodfinder/settings.html", get_context_dict(request), context)

