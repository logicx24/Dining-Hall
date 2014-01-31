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
from string_parser import StringRectifier
from django.conf import settings
from django.views.decorators.csrf import csrf_protect

file_ = open(os.path.join(settings.PROJECT_ROOT, 'menu.txt'))

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
	global request_record
	request_record = request
	context = RequestContext(request)
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			profile.phone = request.POST['phone']
			profile.save()
			registered = True
		else:
			print user_form.errors, profile_form.errors
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render_to_response('foodfinder/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
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
	x = StringRectifier(context_dict['userprofile'].preferences,file_)

	x.remove_crap()
	matches = x.matches()
	html = ""
	for item in matches:
		html += "<div style='margin-bottom: 4px; width: 400px; border-bottom: 1px solid #f0f0f0; float left;'>"
		html += "<strong>"+item[0]+"</strong><br><font color='gray'>during "+item[1]+"</font><br><font color='gray'>at "+item[2]+"</font>"
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

