from django.shortcuts import render, redirect
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, get_permission_codename, login, logout
from django.contrib.auth.models import Permission

# Create your views here.
def signUp(request):
    uform = UserCreationForm(request.POST or None)
    if uform.is_valid():
        uform.save()
        username = uform.cleaned_data.get("username")
        password = uform.cleaned_data.get("password1")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("index")
    return render(request, 'netflixUsers/signup.html',{"uform":uform})

def signIn(request):
    uform = AuthenticationForm()
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username= username, password=password )
        if user:
            login(request, user)
            return redirect("index")
        else:
            return render (request, "netflixUsers/signIn.html", {"uform":uform, "loginAttempt":username})
    return render(request, 'netflixUsers/signIn.html', {"uform":uform})

def logOut(request):
    logout(request)
    return redirect("index")