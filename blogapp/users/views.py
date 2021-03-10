from django.shortcuts import render, redirect
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth import logout
from django.db.models import Count
from django.contrib.auth.models import User
from .models import Profile
from blogs.models import Article
from django.views.generic import DetailView



class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        print(dir(form.data))
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def logoutPage(request):
	logout(request)
	return redirect('login')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    posts = User.objects.annotate(num_posts=Count('article'))
    counts = posts.filter(username = request.user.username)[0]
    post_count = counts.num_posts

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'post_count': post_count
    }
    return render(request, 'users/profile.html', context)

class ProfileDetailView(DetailView):
    model = Profile

    def get_context_data(self, **kwargs):
        user = User.objects.get(id = self.kwargs.get('pk'))
        all_posts = Article.objects.filter(author = user)
        posts = User.objects.annotate(num_posts=Count('article'))
        post_count = posts.filter(username = user.username)[0].num_posts

        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        context['post_count'] = post_count
        context['all_posts'] = all_posts
        return context
