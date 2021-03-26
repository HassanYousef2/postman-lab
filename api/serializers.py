from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from netflix.models import Movie, Cast



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
    password2 = serializers.CharField(write_only=True)
    def save(self, **kwargs):
        user = User(email= self.validated_data.get('email'), username=self.validated_data.get('username'))
        if self.validated_data.get('password') != self.validated_data.get('password2'):
            raise serializers.ValidationError({"password":"password isn't matching!"})
        else:
            user.set_password(self.validated_data.get('password'))
            user.save()


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'rate', 'poster', 'video', 'productionYear']

class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = "__all__"