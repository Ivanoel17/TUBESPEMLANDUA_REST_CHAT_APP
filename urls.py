# chat_app/urls.py
# chat_app/urls.py
from django.urls import path
from .views import DeviceList, MessageList

urlpatterns = [
    path('devices/', DeviceList.as_view(), name='device-list'),
    path('messages/', MessageList.as_view(), name='message-list'),
    # Add other URL patterns as needed
]
