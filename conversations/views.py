from django.shortcuts import render, redirect
from django.utils import timezone
from .models import *
from .forms import MessageForm
# Create your views here.

def inbox(request, profile_friend=None):
    profile = request.user.profile
    friends = profile.friends.all()

    if profile_friend is not None:
        p2 = friends.filter(id=profile_friend).first()
        new_chat = Chat()
        new_chat.save()
        m1 = Chat_members(chat=new_chat, profile=profile, deleted=False, last_viewed=timezone.now())
        m2 = Chat_members(chat=new_chat, profile=p2, deleted=False, last_viewed=timezone.now())
        m1.save()
        m2.save()
        return redirect("conversations:inbox")

    chats_ids = profile.chats.all().values_list('chat_id', flat=True)
    chats = Chat.objects.filter(id__in=chats_ids)
    chatting_with = []

    for c in chats:
        profile_chat_member = c.members.get(profile=profile)
        if profile_chat_member.deleted == False:
            friend_chat_member = c.members.exclude(profile=profile).first()
            chatting_with.append(friend_chat_member)
            friends = friends.exclude(user=friend_chat_member.profile.user)



    context = {
        'profile': profile,
        'friends': friends,
        'chat_details': chatting_with,
    }
    return render(request, 'conversations/inbox.html', context)


def chatbox(request, chat_id):
    profile = request.user.profile
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            new_msg = form.save(commit=False)
            new_msg.profile = profile
            new_msg.chat_id = chat_id
            new_msg.save()
            return redirect('conversations:chatbox', chat_id=chat_id)
    messages = Message.objects.filter(chat_id=chat_id)
    last_viewed = Chat_members.objects.filter(chat_id=chat_id).filter(profile=profile)
    last_viewed.update(last_viewed=timezone.now())

    context = {
        'profile': profile,
        'chat_id': chat_id,
        'form': form,
        'msg': messages,
    }
    return render(request, 'conversations/chatbox.html', context)