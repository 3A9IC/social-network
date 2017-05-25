from django.conf.urls import url,include

from loginsys import views

urlpatterns = [
	#url(r'^login/','loginsys.views.login'),
	#url(r'^logout/','loginsys.views.logout'),
	url(r'^login/', views.login, name='login'),
	url(r'^logout/',views.logout, name='logout'),
]