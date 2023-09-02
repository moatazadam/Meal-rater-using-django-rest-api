from django.urls import path , include
from api import views
from rest_framework import routers
from .views import *
from rest_framework.authtoken.views import obtain_auth_token 

router = routers.DefaultRouter()
router.register('meals' , MealViewSet)
router.register('ratings' , RatingViewSet)
router.register('users' , UserViewSet)


urlpatterns = [
    path('' , include(router.urls)),
    path('token' , obtain_auth_token), # you must provide this URL with username and passsword and it will give you new TOKEN


] 
