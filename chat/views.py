from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Q
from .models import Chat

User = get_user_model()

@login_required
def index(request):
    chats = Chat.objects.filter(Q(participant=request.user) | Q(starter=request.user))

    return render(request, "chat/index.html", context={"chats": chats})

@login_required
def room(request, room_name):
    target_user = User.objects.filter(username=room_name).first()
    if not target_user or room_name == request.user.username:
        raise Http404
    print(target_user)
    chat = Chat.objects.filter((Q(starter=request.user) | Q(participant=request.user)) & (Q(starter=target_user) | Q(participant=target_user))).first()
    print(chat)
    if not chat:
        chat = Chat.objects.create(starter=request.user, participant=target_user)
    return render(request, "chat/room.html", {"room_name": room_name, 'chat': chat})
