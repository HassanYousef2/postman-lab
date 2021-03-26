from django.db import models
from django.db.models.base import Model
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Category(models.Model):
    name = models.fields.CharField(max_length=50)

    def __str__(self):
        return self.name

class Cast(models.Model):
    name = models.fields.CharField(max_length=50)
    age = models.fields.IntegerField()
    address = models.fields.CharField(max_length=70)
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.fields.CharField(max_length=50)
    description = models.fields.TextField()
    productionYear = models.fields.DateField()
    rate = models.fields.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    poster = models.ImageField(upload_to="movies/posters")
    video = models.FileField(upload_to="movies/videos")
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    casts = models.ManyToManyField(Cast)