from django.shortcuts import render, get_object_or_404
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
def room(request, slug):
    chat = get_object_or_404(Chat, slug=slug)
    print(chat)
    target_user = chat.get_target_user(request.user)
    print(target_user)
    return render(request, "chat/room.html", {"room_name": target_user.username, 'chat': chat})
