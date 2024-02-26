from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', about, name='about'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('post/<slug:post_slug>', ShowPost.as_view(), name='post'),
    path('author/<slug:author_slug>', about, name='author'),
    path('profile/<slug:profile_slug>', ShowProfile.as_view(), name='profile'),
]