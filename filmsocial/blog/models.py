from django.db import models

class base_menu(models.Model):
	class Meta():
		db_table = 'Article'
	title = models.CharField(max_length=255) # ссыль на меню
	datetime = models.DateTimeField(u'Дата публикации') # дата публикации
	content = models.TextField(max_length=10000) # название меню
	
	
	
	def __unicode__(self):
		return self.title
	
	def get_absolute_url(self):
		return "/blog/%s/" % self.title
		
class base_col(models.Model):
	class Meta():
		db_table = 'BaseCol'
	title = models.CharField(max_length=255) # заголовок поста
	date = models.CharField(max_length=20) # дата публикации
	url = models.TextField(max_length=10000) # ссыль на источник
	urlpic = models.TextField(max_length=10000) # ссыль картинки
	def __unicode__(self):
		return self.title
	
	def get_absolute_url(self):
		return "/blog/%s/" % self.title
	