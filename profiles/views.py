from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth import authenticate, login
from django.utils import simplejson


def index(request):
	user = request.user
	return render_to_response('index.html', {'user': user,})

def index2(request):
	user = request.user
	return render_to_response('index2.html', {'user': user,})
	


def authenticate_user(request):	
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			message="logged in"
			logged_in="yes"
			
		else:
			message="user not active"
			logged_in="no"			
	else:
		message="The password you entered is incorrect. Please try again."
		logged_in="no"	
	d = { 'message': message, 'logged_in': logged_in }
	return HttpResponse(simplejson.dumps(d))
	