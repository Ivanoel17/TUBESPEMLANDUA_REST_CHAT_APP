from django.shortcuts import render

# Create your views here.
# chat_app/views.py
from rest_framework import generics
from .models import Device, Message
from .serializers import DeviceSerializer, MessageSerializer

class DeviceList(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
