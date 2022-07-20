from django.shortcuts import render

# Create your views here.
#posts.views 
from .models import Post

def home(request):
	posts = Post.objects.all()
	print(posts)