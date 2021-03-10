from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.authtoken import views as token_views

router = routers.DefaultRouter()
router.register('articlesAPI', views.ArticleView)

urlpatterns = [
    path('', include(router.urls))
]

urlpatterns += [
    path('auth/', include('rest_framework.urls')),
    path('api-auth-token/', token_views.obtain_auth_token, name='api-auth-token'),
    path('articles/', views.PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('APIs/', views.api, name='blog-api'),
    path('articles/<int:pk>/', views.PostDetailView.as_view(template_name='blog/post_detail.html'), name='post-detail'),
    path('articles/<int:pk>/update/', views.PostUpdateView.as_view(template_name='blog/post_update.html'), name='post-update'),
    path('articles/<int:pk>/delete/', views.PostDeleteView.as_view(template_name='blog/post_delete_confirm.html'), name='post-delete'),
    path('articles/new/', views.PostCreateView.as_view(template_name='blog/post_create.html'), name='post-create'),
]

