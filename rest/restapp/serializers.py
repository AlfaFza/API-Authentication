from django.contrib.auth import get_user_model

from .models import Task
from rest_framework import serializers

class TaskSerializers(serializers.ModelSerializer):
    img=serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model=Task
        fields=['id','task_name','task_desc','completed','date_created','img']

#creating a new serializers for user authenticationv

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    def create(self, validated_data):
        user=get_user_model().objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    class Meta:
        model=get_user_model()
        fields=('username','password')
