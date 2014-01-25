# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from foodfinder.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def redirection(request):
	context = RequestContext(request)
	return HttpResponseRedirect('/foodfinder/')

def index(request):
	context = RequestContext(request)
	return render_to_response('foodfinder/selection_page.html', context)

def register(request):
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

	return render_to_response('foodfinder/index.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
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
				return HttpResponseRedirect('/foodfinder/')
			else:
				return HttpResponse('Your account was disabled. Bitch.')
		else:
			print "Invalid login details."
			return HttpResponse("Invalid login details supplied. Foiled you, wannabe hacker.")
	else:
		return render_to_response("foodfinder/login.html", {}, context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/foodfinder/')

@login_required
def restricted(request):
	context = RequestContext(request)
	return HttpResponse('Only enter if logged in. Fool.')































