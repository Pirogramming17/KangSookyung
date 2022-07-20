from django.contrib import admin

# Register your models here.
#posts.admin.py 

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass