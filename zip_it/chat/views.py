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
def invite(request):
    if request.user.is_authenticated:
        channels_queryset = Channel.objects.filter(creator=User(request.user.id)).values()
        channels = []
        for channel in channels_queryset:
            channels.append(channel)

        return render(request, 'chat/invite.html', {
            'channels': channels
        })
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

@csrf_exempt
def send_invite(request):
    request_json = json.loads(request.body)

    if not request.user.is_authenticated:
        return HttpResponse(status=401)
    
    # Check if user is actually in channel
    channel = request_json.get("channel", "")
    channel_person = Channel_person.objects.filter(user=User(request.user.id), channel=Channel(channel))
    print(channel_person)
    if channel_person == []:
        return HttpResponse(status=401)

    # Check if user exists
    check_recipient =  User.objects.filter(username=request_json.get("recipient", ""))
    if check_recipient == []:
        return HttpResponse(status=404)

    # Make sure recipient is not already in channel
    channel_person_recipient = Channel_person.objects.filter(channel=Channel(channel), user=User.objects.get(username=request_json.get("recipient", ""))).values()
    
    if channel_person_recipient[0] != {}:
        return HttpResponse(status=409)

    # Check if already sent invite
    check_invite = Invite.objects.filter(sender=User(request.user.id), reciever=User.objects.get(username=request_json.get("recipient", ""), channel=request_json.get("channel", ""))).values()
    if check_invite[0] != {}:
        return HttpResponse(status=409)

    invite = Invite(sender=User(request.user.id), reciever=User.objects.get(username=request_json.get("recipient", "")), channel=Channel(request_json.get("channel", "")))
    invite.save()
    return HttpResponse(status=200)

def list_invites(request):
    invites_object = Invite.objects.filter(reciever=User(request.user.id), accepted=False)
    invites_queryset = Invite.objects.filter(reciever=User(request.user.id), accepted=False).values()
    invites = []
    i = 0
    for invite in invites_object:
        dict = invites_queryset[i]
        print(invite)
        print(type(invite.channel.name))
        dict["channel_name"] = str(invite.channel.name)
        invites.append(dict)
        print('invite!')
        i += 1
    print(invites)
    return JsonResponse(invites, safe=False)

@csrf_exempt
def accept_invite(request):
    request_json = json.loads(request.body)

    if not request.user.is_authenticated:
        return HttpResponse(status=401)

    invite = Invite.objects.filter(reciever=User(request.user.id), id=int(request_json.get("invite_id", ""))).values()
    if invite[0] == {}:
        return HttpResponse(status=404)

    invite = Invite.objects.get(reciever=User(request.user.id), id=int(request_json.get("invite_id", "")))
    invite.accepted = True
    invite.save()

    print(invite.channel.name)
    channel_person = Channel_person(user=User(request.user.id), channel=Channel(invite.channel.id))
    channel_person.save()
    return HttpResponseRedirect('/channel/'+str(invite.channel.id))

@csrf_exempt
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

def user(request, id):
    userqueryset = User.objects.filter(id=id).values()
    user = userqueryset[0]
    return JsonResponse(user['username'], safe=False)


@csrf_exempt
def message(request):
    request_json = json.loads(request.body)

    if not request.user.is_authenticated:
        return HttpResponse(status=401)

    channel = request_json.get("channel", "")
    text = request_json.get("text", "")

    if Channel_person.objects.filter(channel=Channel(int(channel)), user=User(request.user.id)).values()[0] == {}:
        return HttpResponse(status=401)

    message = Channel_message(channel=Channel(int(channel)), user=User(request.user.id), text=text)
    message.save()

    return HttpResponse(status=200)

def messages(request, channel_id):
    if not request.user.is_authenticated:
        return HttpResponse(status=401)

    if Channel_person.objects.filter(channel=Channel(int(channel_id)), user=User(request.user.id)).values()[0] == {}:
        return HttpResponse(status=401)

    messages_queryset = Channel_message.objects.filter(channel=Channel(channel_id)).order_by('-id').values()
    messages = []
    for message in messages_queryset:
        messages.append(message)

    print(messages)
    return JsonResponse(messages, safe=False)

def channelAPI(request, id):
    if not request.user.is_authenticated:
        return HttpResponse(status=401)

    channel = Channel.objects.filter(id=int(id)).values()
    channel = channel[0]
    return JsonResponse(channel, safe=False)