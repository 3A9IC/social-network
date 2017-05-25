from django.shortcuts import render,render_to_response,redirect
from blog.models import base_menu 
from django.contrib import auth
from django.template.context_processors import csrf


def login(request):
	args = {}
	args.update(csrf(request))
	#args.update(request)
	if request.POST:
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('/blog')#!!!!
		else:
			args['login_error'] = "Пользователь не найден"
			#return render_to_response('login.html', args)
			return render(request, 'loginsys/login.html', args )
			#return render(request, 'loginsys/login.html')
	else:
		#return render_to_response('login.html', args)
		return render(request, 'loginsys/login.html', args ) #добавляет строчку ВХОД в меню на ссылку /auth/login/
		#return render(request, 'loginsys/login.html')

def logout(request):
	auth.logout(request)
	return redirect("/blog")