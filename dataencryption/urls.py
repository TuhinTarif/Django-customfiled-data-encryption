from rest_framework import routers
from .views import UserProfileViewSet
from django.urls import path, include

me_router = routers.DefaultRouter()
me_router.register('profile', UserProfileViewSet, basename='userprofile')


urlpatterns = [
    #me router
    path('', include(me_router.urls)),]