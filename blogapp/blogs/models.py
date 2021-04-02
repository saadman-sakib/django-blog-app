from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Article(models.Model):
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
    	return self.title

    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})

    @property
    def snippet(self):
        body_list = self.content.split(' ')

        if len(body_list) > 30:
            return ' '.join(body_list[:30]) + '......'

        return self.content