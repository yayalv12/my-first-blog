from django.contrib import admin
from .models import Post #Post model defined on models.py

admin.site.register(Post) #make our model visible on the admin page