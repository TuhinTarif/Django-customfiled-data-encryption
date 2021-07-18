from rest_framework import serializers, validators
from .models import UserProfile

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['url', 'id','bank_name','bank_account']