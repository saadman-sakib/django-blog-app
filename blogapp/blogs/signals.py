from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Article
import time
import socketio



@receiver(post_save, sender=Article)
def push(sender, instance, created, **kwargs):
    if created:
        sio = socketio.Client()
        sio.connect('https://django-socket-server.herokuapp.com')
        time.sleep(2)
        sio.emit('chat', instance.author.username)
        print("gg")