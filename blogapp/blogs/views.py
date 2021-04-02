from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrAnonReadOnly

from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Article


class PostListView(ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-date_created']


class PostDetailView(DetailView):
    model = Article


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

#api
class ArticleView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    #added for authentication
    authetication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAuthorOrAnonReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


def about(request):
    return render(request, 'blog/about.html')

def api(request):
    return render(request, 'blog/api.html')



