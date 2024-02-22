from django.contrib import admin

from .models import *


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'name', 'surname')
    list_display_links = ('id', 'name')
    search_fields = ('id', )
    list_filter = ('id', )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'content')
    list_display_links = ('id', )
    search_fields = ('id', 'title', 'content')
    list_filter = ('id', 'title')
    prepopulated_fields = {'slug': ('title', )}
