from django.db import models
from django.contrib.auth import get_user_model
from random import randint

User = get_user_model()

app_name = 'chat'

class Chat(models.Model):
    starter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='started_chats')
    participant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='participated_chats')
    slug = models.SlugField(null=True, blank=True)
    start_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = randint(1000000000000000, 9999999999999999)
        return super(Chat, self).save(*args, **kwargs)

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sended_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    send_date = models.DateTimeField(auto_now_add=True)