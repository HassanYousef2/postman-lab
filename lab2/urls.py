"""lab2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from netflix.views import view
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register('vsusers', views.UserViewSet)
router.register('vsmovies', views.MovieViewSet)
router.register('vscast',views.CastViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('netflix/', include('netflix.urls')),
    path('users/', include('netflixUsers.urls')),
    path('api/',include(router.urls)),
    path('api/', include("api.urls")),
    
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)