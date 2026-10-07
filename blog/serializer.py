from django.contrib.auth.models import User
from rest_framework import serializers
from .models import blogpost

class Blogpostserializer(serializers.ModelSerializer):
    class Meta:
        model = blogpost
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']

    def create(self, validated_data):
        user=User.objects.create_user(validated_data['username'],validated_data['password'])
        return user