from django.urls import path
from . import views

urlpatterns = [
    path("signup", views.signUp, name="signUp"),
    path("logout", views.logOut, name="logOut"),
    path("signin", views.signIn, name="signIn")
]