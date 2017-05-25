from django.db import models

class base_menu(models.Model):
	class Meta():
		db_table = 'Article'
	title = models.CharField(max_length=255) # заголовок поста
	datetime = models.DateTimeField(u'Дата публикации') # дата публикации
	content = models.TextField(max_length=10000) # текст поста
	
	
	
	def __unicode__(self):
		return self.title
	
	def get_absolute_url(self):
		return "/blog/%s/" % self.title