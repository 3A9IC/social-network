from django.contrib import admin

from blog.models import base_menu, base_col # наша модель из blog/models.py

admin.site.register(base_menu)
admin.site.register(base_col)