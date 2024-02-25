from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    first_name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Surname', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['slug'].label = 'URL'

    class Meta:
        model = Post
        fields = ['title', 'slug', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 10})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Length exceeds 200 symbols')
        return title

    def save(self, commit=True):
        user = self.request.user
        post = super().save(commit=False)
        post.author = user.author
        if commit:
            post.save()
        return post
