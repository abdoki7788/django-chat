import json

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from django.db.models import Q
from .models import Message, Chat, User

class ChatConsumer(AsyncJsonWebsocketConsumer):
    @database_sync_to_async
    def get_chat_room(self):
        return Chat.objects.filter(slug=self.scope['url_route']['kwargs']['slug']).first()
    @database_sync_to_async
    def get_target_user(self):
        chat = Chat.objects.filter(slug=self.scope['url_route']['kwargs']['slug']).first()
        return chat.get_target_user(self.scope['user'])
    @database_sync_to_async
    def create_message(self, message): 
        return Message.objects.create(content=message, sender=self.scope['user'], receiver=self.target_user, chat=self.target_chat)
    
    async def connect(self):
        if not self.scope['user'].is_authenticated:
            print('not authenticated')
            await self.close()
        self.room_name = self.scope['url_route']['kwargs']['slug']
        self.target_user = await self.get_target_user()
        self.target_chat = await self.get_chat_room()
        self.room_group_name = f"chat_{str(self.room_name)}"

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
    
    async def disconnect(self, code):
        print(code)
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
    
    async def receive_json(self, content):
        message = await self.create_message(content['message'])
        content['sender'] = self.scope['user'].username
        print(message.send_date)
        content['date'] = message.send_date.strftime("%b. %d, %Y, %H:%M %p")
        await self.channel_layer.group_send(self.room_group_name, {'type': 'chat_message', 'message':content})

    async def chat_message(self, event):
        await self.send_json(content=event['message'])