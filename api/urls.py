from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('castCR/', views.castListCreate),
    path('castRUD/<int:id>/', views.castRetrieveUpdate),
    path("login/", obtain_auth_token),
    path("castGCR/",views.castGenericCR.as_view()),
    path("castGRUD/<int:pk>",views.castGenericRUD.as_view()),
]