from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Movie, Category, Cast
# Register your models here.

class MovieStacked(admin.StackedInline):
    model = Movie
    extra = 1 
    max_num = 5 

class CategoryAdmin(admin.ModelAdmin):
    inlines = [MovieStacked]

class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "productionYear","rate", "category") 
    list_filter = ("productionYear", "category")

admin.site.register(Movie, MovieAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Cast)