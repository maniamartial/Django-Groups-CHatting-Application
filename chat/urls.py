from .import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:room_name>/', views.room, name='room'),
    path('bot', views.chatting, name='bot')
]
