
from .views import RegisterView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views


urlpatterns = [
    path('registerAPI/', RegisterView.as_view()),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('profile/<int:pk>/', user_views.ProfileDetailView.as_view(template_name='users/profile_detail.html'), name='profile-detail'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', user_views.logoutPage, name='logout'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)