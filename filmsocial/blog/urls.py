from django.conf.urls import url,include

from blog import views


urlpatterns = [
	url(r'^$', views.basemenu, name="basemenu"),
	url(r'^mainpage/$', views.main_page, name='main'),
	url(r'^news', views.news, name='news'),
	url(r'^groups/$', views.groups, name='groups'),
	url(r'^message/$', views.message, name='message'),
]