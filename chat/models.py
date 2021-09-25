from django.db import models
from Member.models import *
from django.utils import timezone
# Create your models here.


class ChatRoom(models.Model):
    name = models.CharField(max_length=100, null=False)
    creator = models.ForeignKey(Member, on_delete=models.CASCADE, null=False, blank=False, related_name='my_chatrooms')
    created_time = models.DateTimeField()
    timestamp = models.DateTimeField(default=timezone.now)
    '''participants가 있어야 함'''
    participants = models.ManyToManyField(Member, through='Member_ChatRoom', related_name='chats')


class Member_ChatRoom(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    member_timestamp = models.DateTimeField() # 멤버가 나간 시간 -> develop : 멤버가 지금 채팅방에 머물지 않고 있을 때
    chat_room_timestamp = models.DateTimeField() # 가장 최신의 채팅 시간


class Message(models.Model):
    message = models.TextField(null=False, blank=False)
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, null=False, blank=False)
    sender = models.ForeignKey(Member, on_delete=models.CASCADE, null=False, blank=False, related_name='my_messages')
    timestamp = models.DateTimeField()

