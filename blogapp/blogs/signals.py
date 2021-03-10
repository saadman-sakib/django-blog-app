from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Article
import time



@receiver(post_save, sender=Article)
def push(sender, instance, created, **kwargs):
    if created:
        import socketio
        sio = socketio.Client()
        sio.connect('http://192.168.43.189:7000')
        time.sleep(.1)
        sio.emit('chat', instance.author.username)