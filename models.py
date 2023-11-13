from django.db import models

# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=255)

class Message(models.Model):
    sender = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)