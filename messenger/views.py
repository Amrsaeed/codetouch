from django.shortcuts import render
from django.http import HttpResponse
from .models import Message

# Create your views here.


def index(request):
    latest_message_list = Message.objects.order_by('-sent')[:5]
    context = {'latest_message_list': latest_message_list}
    return render(request, 'messenger/index.html', context)

def detail(request, id):
    return HttpResponse(id)