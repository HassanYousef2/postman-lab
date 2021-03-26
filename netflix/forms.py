from django.forms import ModelForm, fields
from . import models

class MovieForm(ModelForm):
    class Meta:
        model = models.Movie
        fields = "__all__"