from django.shortcuts import render, get_object_or_404, redirect
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
    chats = Chat.objects.filter(Q(participant=request.user) | Q(starter=request.user))
    target_user = chat.get_target_user(request.user)
    return render(request, "chat/room.html", {"room_name": target_user.username, 'chat': chat, 'chats': chats})

@login_required
def add_friend(request):
    if request.method == 'POST':
        user = User.objects.filter(username=request.POST['name']).first()
        if user and not Chat.objects.filter((Q(starter=user) | Q(participant=user)) & (Q(starter=request.user) | Q(participant=request.user))):
            chat = Chat.objects.create(starter=request.user, participant=user)
            return redirect("chat:room", slug=str(chat.slug))
        else:
            return redirect("chat:index")