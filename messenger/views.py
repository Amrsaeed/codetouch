from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from .models import Message
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.core import serializers
import datetime
import json

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('messenger:webchat'))

    return render(request, 'messenger/index.html')


def signin(request):
    user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
    if user is not None:
        login(request, user)
        request.session.set_expiry(0)  # Expire session on browser close
        return HttpResponseRedirect(reverse('messenger:webchat'))
    else:
        context = {'error_message': 'Login Failed'}
        return render(request, 'messenger/index.html', context)


def signup(request):
    first_name = request.POST.get('fname')
    last_name = request.POST.get('lname')
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')

    # Check for duplicate username
    try:
        u = User.objects.get(username=username)
    except User.DoesNotExist:
        u = None

    # Check for duplicate email
    try:
        e = User.objects.get(email=email)
    except User.DoesNotExist:
        e = None

    if u is not None:
        context = {'error_message': 'User Exists'}
        return render(request, 'messenger/index.html', context)

    if e is not None:
        context = {'error_message': 'Email Exists'}
        return render(request, 'messenger/index.html', context)

    user = User.objects.create_user(first_name=first_name, last_name=last_name,
                                    username=username, password=password,
                                    email=email)

    context = {'user_created': 'User Created'}
    return render(request, 'messenger/index.html', context)


def datetime_handler(x):
    if isinstance(x, datetime.datetime):
        time = str(x.hour)+":"+str(x.minute)+":"+str(x.second)
        # return x.isoformat()
        return time
    raise TypeError("Unknown type")

@login_required(login_url='/')
def webchat(request):
    secondary_user = request.POST.get('secondary_user')
    print(secondary_user)
    message_text = request.POST.get('message')

    if message_text:
        message = Message(message_text=message_text,
                          sentOn=timezone.now(),
                          sender=request.user,
                          reciever=secondary_user)
        message.save()

    sessions = Session.objects.filter(expire_date__gte=timezone.now())
    uid_list = []

    # Build a list of user ids from that query
    for session in sessions:
        data = session.get_decoded()
        uid_list.append(data.get('_auth_user_id', None))

    # Query all logged in users based on id list
    online_users = User.objects.filter(id__in=uid_list)
    offline_users = []
    users = User.objects.all()
    for user in users:
        if user not in online_users:
            offline_users.append(user)

    recieved_messages = Message.objects.filter(reciever=request.user, sender=secondary_user).values()
    sent_messages = Message.objects.filter(sender=request.user, reciever=secondary_user).values()

    if recieved_messages is None and sent_messages is None:
        context = {'online_users': online_users,
                   'offline_users': offline_users,
                   'main_user': request.user,
                   'No Messages': 'Send a message now to begin the conversation'}

        return render(request, 'messenger/webchat.html', context)

    messages = recieved_messages | sent_messages
    messages = messages.order_by('sentOn')
    context = {'online_users': online_users,
               'offline_users': offline_users,
               'main_user': request.user,
               'secondary_user': secondary_user,
               'Messages': messages}

    if request.is_ajax() and request.method == 'POST':
        context = {'Messages': messages, 'secondary_user': secondary_user, 'main_user': request.user}
        return render(request, 'messenger/chatbody.html', context)
        # return render(request, 'messenger/webchat.html', context)
    else:
        return render(request, 'messenger/webchat.html', context)


def signout(request):
    print('Ana geet')
    logout(request)
    return HttpResponseRedirect(reverse('messenger:index'))

