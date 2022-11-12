from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

app_name = 'chat'

class Chat(models.Model):
    starter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='started_chats')
    participant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='participated_chats')
    start_date = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sended_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    send_date = models.DateTimeField(auto_now_add=True)