from django.urls import path
from .views import *

app_name = 'conversations'

urlpatterns = [
    path('inbox/', inbox, name='inbox'),
    path('inbox/<int:profile_friend>', inbox, name='inbox_new_chat'),
    path('chatbox/<int:chat_id>', chatbox, name='chatbox'),
]