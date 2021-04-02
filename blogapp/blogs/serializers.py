from rest_framework import serializers
from .models import Article
from django.contrib.auth.models import User

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('username',)
        model = User


class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    
    class Meta:
        model = Article
        fields = ('id','title', 'author', 'content',)