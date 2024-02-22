from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Author


@receiver(post_save, sender=get_user_model())
def create_author(sender, instance, created, **kwargs):
    if created:
        Author.objects.create(user=instance, slug=instance.username)


@receiver(post_save, sender=get_user_model())
def save_author(sender, instance, **kwargs):
    instance.author.save()