from django.shortcuts import redirect, render
from .models import Post

# Create your views here.
def home(request):
    reviews = Post.objects.all()

    context = {
        "posts" : reviews
    }

    return render(request, template_name="posts/home.html", context=context)

def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        release = request.POST["release"]
        genre = request.POST["genre"]
        star = request.POST["star"]
        time = request.POST["time"]
        content = request.POST["content"]
        director = request.POST["director"]
        actor = request.POST["actor"]

        Post.objects.create(title=title, release=release, genre=genre, star=star, time=time, content=content, director=director, actor=actor)
        return redirect("/")
    
    else:
        context = {}
        return render(request, template_name="posts/create.html", context=context)

def detail(request, id):
    review = Post.objects.get(id=id)

    context = {
        "review" : review
    }

    return render(request, template_name="posts/detail.html", context=context)

def modify(request, id):
    if request.method == "POST":
        title = request.POST["title"]
        release = request.POST["release"]
        genre = request.POST["genre"]
        star = request.POST["star"]
        time = request.POST["time"]
        content = request.POST["content"]
        director = request.POST["director"]
        actor = request.POST["actor"]

        Post.objects.filter(id=id).update(title=title, release=release, genre=genre, star=star, time=time, content=content, director=director, actor=actor)
        return redirect(f"/review/{id}")
    else:
        review = Post.objects.get(id=id)
        context = {
            "review" : review
        }
        return render(request, template_name="posts/modify.html", context=context)
def delete(request, id):
    if request.method == "POST":
        Post.objects.filter(id=id).delete()
    return redirect("/")