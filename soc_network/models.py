from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    friends = models.ManyToManyField('self', blank=True)
    liked_posts = models.ManyToManyField('Post', related_name='liked_by_authors', blank=True)

    def save(self, *args, **kwargs):
        self.name = self.user.first_name
        self.surname = self.user.last_name
        self.slug = self.user.username
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('author', kwargs={'author_slug': self.slug})

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ['id']


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('Author', on_delete=models.PROTECT, related_name='posts')
    liked_by = models.ManyToManyField('Author', related_name='liked_posts_posts', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['id']



