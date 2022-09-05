from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass
    def __str__(self):
        return f"{self.username}" 

class Channel(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="channels")
    name = models.TextField(max_length=25)
    def __str__(self):
        return f"{self.name}" 

class Channel_person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="channels_in")
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name="people")
    def __str__(self):
        return f"'{self.user.username}' is in the '{self.channel.name}' channel" 

class Channel_message(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="messages")
    text = models.TextField()
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name="channel_messages")
    def __str__(self):
        return f"'{self.user.username}' texted in '{self.channel.name}'" 

class Invite(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sending")
    reciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recieving")
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name="sent_invites")
    accepted = models.BooleanField(default=False)
    def __str__(self):
        return f"'{self.sender.username}' invited '{self.reciever.username}' to '{self.channel.name}'" 
