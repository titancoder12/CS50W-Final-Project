from django.contrib import admin
from .models import User, Channel, Channel_person, Channel_message, Invite

# Register your models here.
admin.site.register(User)
admin.site.register(Channel)
admin.site.register(Channel_person)
admin.site.register(Channel_message)
admin.site.register(Invite)