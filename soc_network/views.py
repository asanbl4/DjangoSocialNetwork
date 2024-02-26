from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from .forms import *
from .utils import DataMixin
from .models import *

menu = [
        {'title': "About the website", 'url_name': 'about'},
        {'title': "Add post", 'url_name': 'add_post'},
        ]


class Home(DataMixin, ListView):
    model = Post
    template_name = 'soc_network/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Home')
        return dict(list(context.items()) + list(c_def.items()))


class ShowProfile(DataMixin, DetailView):
    model = Author
    slug_url_kwarg = 'profile_slug'
    template_name = 'soc_network/profile.html'
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=f"Profile")
        return dict(list(context.items()) + list(c_def.items()))


class ShowPost(DataMixin, DetailView):
    model = Post
    slug_url_kwarg = 'post_slug'
    template_name = 'soc_network/post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


def about(request):
    return HttpResponse('about')


class AddPost(DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'soc_network/add_post.html'
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Add post')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        form.request = self.request
        return super().form_valid(form)


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'soc_network/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Sign up')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'soc_network/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Log in')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')


def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Page not found!</h1>")




