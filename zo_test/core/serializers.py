from rest_framework import serializers
from .models import UserTest

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserTest
        fields = ['name', 'phone_number']


class UserSerializerTwo(serializers.ModelSerializer):

    class Meta:
        model = UserTest
        exclude = ['name', 'phone_number']