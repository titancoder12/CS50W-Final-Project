from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Channel(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="channels")
    name = models.TextField(max_length=25)

class Channel_person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="channels_in")
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name="people")

class Channel_message(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="messages")
    text = models.TextField()
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name="channel_messages")

class Invite(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sending")
    reciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recieving")
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name="sent_invites")
    accepted = models.BooleanField(default=False)
