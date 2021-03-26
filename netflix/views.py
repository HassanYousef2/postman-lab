from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Movie
from .forms import MovieForm
# Create your views here.

def index(request):
    movies = Movie.objects.all()
    return render(request, 'netflix/index.html', {"movies":movies})

@login_required(login_url="signIn")
@permission_required("netflix.add_Movie", raise_exception=True)
def add(request):
    mform = MovieForm(request.POST or None, request.FILES or None)
    if mform.is_valid():
        mform.save()
        return redirect("index")

    return render(request, 'netflix/add.html', {"mform":mform})

@login_required(login_url="signIn")
@permission_required("netflix.change_Movie", raise_exception=True)
def update(request, id):
    movie = Movie.objects.get(pk=id)
    mform = MovieForm(request.POST or None, request.FILES or None, instance=movie)
    if mform.is_valid():
        mform.save()
        return redirect("index")
    
    return render(request, 'netflix/update.html', {"mform":mform, "movie":movie})
    

@login_required(login_url="signIn")
@permission_required("netflix.delete_Movie", raise_exception=True)
def delete(request, id):
    movie = Movie.objects.get(pk=id)
    movie.delete()
    return redirect("index")

@login_required(login_url="signIn")
def view(request, id):
    movie = Movie.objects.get(pk=id)
    return render(request, 'netflix/view.html', {"movie":movie})