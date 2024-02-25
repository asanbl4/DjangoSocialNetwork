# Generated by Django 4.2.10 on 2024-02-21 18:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("surname", models.CharField(max_length=100)),
                ("slug", models.SlugField(max_length=100, unique=True)),
                (
                    "friends",
                    models.ManyToManyField(blank=True, to="soc_network.author"),
                ),
            ],
            options={
                "verbose_name": "Author",
                "verbose_name_plural": "Authors",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("slug", models.SlugField(max_length=255, unique=True)),
                ("content", models.TextField(blank=True)),
                ("time_create", models.DateTimeField(auto_now_add=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="posts",
                        to="soc_network.author",
                    ),
                ),
                (
                    "liked_by",
                    models.ManyToManyField(
                        blank=True,
                        related_name="liked_posts_posts",
                        to="soc_network.author",
                    ),
                ),
            ],
            options={
                "verbose_name": "Post",
                "verbose_name_plural": "Posts",
                "ordering": ["id"],
            },
        ),
        migrations.AddField(
            model_name="author",
            name="liked_posts",
            field=models.ManyToManyField(
                blank=True, related_name="liked_by_authors", to="soc_network.post"
            ),
        ),
        migrations.AddField(
            model_name="author",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]