from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Message
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    logout(request)
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('messenger:webchat'))

    return render(request, 'messenger/index.html')


def signin(request):
    user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
    if user is not None:
        login(request, user)
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

    try:
        u = User.objects.get(username=username)
    except User.DoesNotExist:
        u = None

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


@login_required(login_url='/')
def webchat(request):
    return HttpResponse('Chat Page')

