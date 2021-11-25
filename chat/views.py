from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.


def home(request):
    return render(request, 'blog/index.html')


def room(request, room_name):
    context = {'room_name': room_name}
    return render(request, "blog/room.html", context)


def chatting(request):
    return render(request, "blog/chatting.html")
