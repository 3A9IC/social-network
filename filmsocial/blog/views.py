#from __future__import unicode_literals
#from future import unicode_literals
from django.shortcuts import render,render_to_response
from blog.models import base_menu
from django.views.generic import ListView, DetailView
from django.contrib import auth



class PostsListView(ListView): # представление в виде списка
    model = base_menu                  # модель для представления 

#class PostDetailView(DetailView): # детализированное представление модели
#    model = Post

def basemenu(request):
	#return render_to_response('post_list.html', {'username': auth.get_user(request)})
	return render(request, 'blog/base_menu_list.html', {'basemenu': base_menu.objects.all(), 'username': auth.get_user(request).username})
	#return render(request, 'blog/base_menu_list.html', {'username': auth.get_user(request)})
#class mainpage2(ListView):
#	return render_to_response('main_page.html')
	
def main_page(request):
	return render(request, 'blog/mainpage.html')

def news(request):
	return render(request, 'blog/news.html')
	
def groups(request):
	return render(request, 'blog/groups.html')
	
def message(request):
	return render(request, 'blog/message.html')