from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("channel/<int:id>", views.channel, name='channel'),
    path("tutorial/", views.tutorial, name='tutorial'),
    path("channels", views.channels, name='channels'),
    path("invites", views.invites, name='invites'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),

    # API Routes
    path("api/channels", views.channelsAPI, name='channels_api'),
    path("api/createchannel", views.newchannel, name='new_channel'),
    path("api/invites", views.list_invites, name="list_invites"),
    path("api/sendinvite", views.send_invite, name="send_invite"),
    path("api/accept_invite", views.accept_invite, name="accept_invite"),
    path("api/decline_invite", views.decline_invite, name="decline_invite"),

]