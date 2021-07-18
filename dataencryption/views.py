from django.shortcuts import render
from rest_framework import viewsets
from .models import UserProfile
from .serializer import UserProfileSerializer

# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()

