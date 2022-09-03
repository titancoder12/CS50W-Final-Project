from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db import IntegrityError
from .models import User, Channel, Channel_person, Channel_message, Invite
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def login_view(request):
    logout(request)
    print(request.GET.get('next'))
    next = request.GET.get('next')
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            #next = 0
            #print(request.GET.get('next'))
            if not next:
                return HttpResponseRedirect(reverse("index"))
            else: 
                return HttpResponseRedirect(next)
        else:
            return render(request, "chat/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        #print(request.GET.get('next'))
        return render(request, "chat/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    logout(request)
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "chat/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "chat/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "chat/register.html")

def index(request):
    return render(request, 'chat/index.html')

#@login_required(redirect_field_name=None)
def channel(request, id):
    if request.user.is_authenticated:
        return render(request, 'chat/channel.html')
    else:
        return render(request, 'chat/error.html', {
            'error_header': '401 Unauthorized',
            'error_discription': 'Click <a href=\'/login\'>here</a> to log in before you vist this page.' 
        })

def tutorial(request):
    return render(request, 'chat/tutorial.html')

def channels(request):
    if request.user.is_authenticated:
        return render(request, 'chat/channels.html')
    else:
        return render(request, 'chat/error.html', {
            'error_header': '401 Unauthorized',
            'error_discription': 'Click <a href=\'/login\'>here</a> to log in before you vist this page.' 
        })

def invites(request):
    if request.user.is_authenticated:
        return render(request, 'chat/invites.html')
    else:
        return render(request, 'chat/error.html', {
            'error_header': '401 Unauthorized',
            'error_discription': 'Click <a href=\'/login\'>here</a> to log in before you vist this page.' 
        })

# API Views

def channelsAPI(request):
    if not request.user.is_authenticated:
        return HttpResponse(status=401)
    channels_in = Channel_person.objects.filter(user=User(request.user.id)).values()
    channels = []
    i=0
    for channel_in in channels_in:
        channel = Channel.objects.filter(id=channel_in["channel_id"]).values()
        print(channel[0])
        channels.append(channel[0])
        i+=1


    return JsonResponse(channels, safe=False)

@csrf_exempt
def newchannel(request):
    request_json = json.loads(request.body)

    if not request.user.is_authenticated:
        return HttpResponse(status=401)
    
    channel = Channel(creator=User(request.user.id), name=request_json.get("channel_name", ""))
    channel.save()

    channel_person = Channel_person(user=User(request.user.id), channel=Channel(channel.id))
    channel_person.save()
    return HttpResponse(status=200)

def send_invite(request):
    request_json = json.loads(request.body)

    if not request.user.is_authenticated:
        return HttpResponse(status=401)
    
    # Check if user is actually in channel
    channel = request_json.get("channel", "")
    channel_person = Channel_person.objects.filter(user=User(request.user.id), channel=Channel(channel))

    if channel_person[0] == {}:
        return HttpResponse(status=401)

    # Make sure recipient is not already in channel
    channel_person_recipient = Channel_person.objects.filter(channel=Channel(channel), user=User(request_json.get("recipient", "")))
    
    if channel_person[0] != {}:
        return HttpResponse(status=409)

    invite = Invite(sender=User(request.user.id), reciever=User(request_json.get("recipient", "")), channel=Channel(request_json.get("channel", "")))
    invite.save()
    return HttpResponse(status=200)

def list_invites(request):
    invites_queryset = Invite.objects.filter(reciever=User(request.user.id), accepted=False)
    invites = []
    for invite in invites_queryset:
        dict = invite
        dict["channel_name"] = str(invite.channel.name)
        invites.append(dict)
        print('invite!')
    print(invites)
    return invites

def accept_invite(request):
    request_json = json.loads(request.body)

    if not request.user.is_authenticated:
        return HttpResponse(status=401)

    invite = Invite.objects.filter(reciever=User(request.user.id), id=request_json.get("invite_id", "")).values()
    if invite[0] == {}:
        return HttpResponse(status=404)

    invite = Invite.objects.get(reciever=User(request.user.id), id=request_json.get("invite_id", ""))
    invite.accepted = True
    invite.save()

    channel_person = Channel_person(user=User(request.user.id), channel=Channel(invite.channel))
    channel_person.save()
    return HttpResponseRedirect('/channel/'+invite.channel)

def decline_invite(request):
    request_json = json.loads(request.body)

    if not request.user.is_authenticated:
        return HttpResponse(status=401)

    invite = Invite.objects.filter(reciever=User(request.user.id), id=request_json.get("invite_id", "")).values()
    if invite[0] == {}:
        return HttpResponse(status=404)
    
    invite = Invite.objects.get(reciever=User(request.user.id), id=request_json.get("invite_id", ""))
    invite.delete()
    return HttpResponse(status=200)

