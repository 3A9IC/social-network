from django.shortcuts import render,render_to_response,redirect
from blog.models import base_menu 
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm


def login(request):
	args = {}
	args.update(csrf(request))
	username1 = request.POST.get('Username')
	password1 = request.POST.get('Password', '')
	user = authenticate(username=username1, password=password1)
	if user is not None:
		auth.login(request, user)
		return redirect('/blog')
	else:
		args['login_error'] = "Пользователь не найден"
		return render(request, 'loginsys/login.html', args )

def logout(request):
	auth.logout(request)
	return redirect("/blog")
	
def register(request):
	args = {}
	args.update(csrf(request))
	args['form'] = UserCreationForm()
	if request.POST:
		newuser_form = UserCreationForm(request.POST)
		if newuser_form.is_valid():
			newuser_form.save()
			return redirect('/blog')
		else:
			args['form'] = newuser_form
	return render(request, 'loginsys/register.html', args)