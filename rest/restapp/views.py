from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import *
from .models import Task
from rest_framework.generics import CreateAPIView

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('date_created')
    serializer_class = TaskSerializers
    permission_classes = (IsAuthenticated,)
class DueTaskViewset(viewsets.ModelViewSet):
    serializer_class = TaskSerializers
    queryset = Task.objects.all().order_by('date_created').filter(completed=False)
class CompletedTaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('date_created').filter(completed=True)
    serializer_class = TaskSerializers


    #for authentication

class createUserView(CreateAPIView):
    model=get_user_model()
    permission_classes=(AllowAny,)
    serializer_class=UserSerializer

