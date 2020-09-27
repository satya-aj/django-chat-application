from django.contrib import admin
from .models import Chat, Chat_members, Message
# Register your models here.


admin.site.register(Chat)
admin.site.register(Chat_members)
admin.site.register(Message)