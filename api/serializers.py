from rest_framework import serializers
from .models import *
from rest_framework.authtoken.models import Token

class MealSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Meal
        fields = ['id' , 'title' , 'description', 'no_of_ratings' , 'avg_rating']


class RatingSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Rating
        fields = ['id' , 'stars', 'user' , 'meal']

class UserSerializer(serializers.ModelSerializer) :
    class Meta :
        model = User 
        fields = [ 'id' , 'username' , 'password']

        def create(self , validated_data) :
            user = User.objects.create(**validated_data)
            Token.objects.create(user=user)
            return user