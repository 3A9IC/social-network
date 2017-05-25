from django.conf.urls import url,include

from blog import views
from blog.views import PostsListView#, PostDetailView

urlpatterns = [
	url(r'^$', views.basemenu, name="basemenu"),
	url(r'^$', PostsListView.as_view(), name='list'), # то есть по URL http://имя_сайта/blog/ 
                                               # будет выводиться список постов
	
	#url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()),  а по URL http://имя_сайта/blog/число/ 
                                              # будет выводиться пост с определенным номером
	url(r'^mainpage/$', views.main_page, name='main'),
	url(r'^news', views.news, name='news'),
	url(r'^groups/$', views.groups, name='groups'),
	url(r'^message/$', views.message, name='message'),
	#url(r'^/3', mainpage2.as_view()),
]