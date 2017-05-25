from django.shortcuts import render,render_to_response
from blog.models import base_menu, base_col
from django.contrib import auth



def basemenu(request):
	return render(request, 'blog/base_menu_list.html', {'basemenu': base_menu.objects.all(), 'username': auth.get_user(request).username, 'base_col': base_col.objects.all(),})
def main_page(request):
	return render(request, 'blog/mainpage.html')

def news(request):
	return render(request, 'blog/news.html')
	
def groups(request):
	return render(request, 'blog/groups.html')
	
def message(request):
	return render(request, 'blog/message.html')