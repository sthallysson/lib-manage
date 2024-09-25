from django.contrib import admin
from libary import models

# Register your models here.


@admin.register(models.Collection)
class LibaryAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'author', 'year', 'isbn', 'type', 'book_count', 'type', 'genre', 'description',
    ordering = 'title',
    search_fields = 'id', 'title', 'author', 'year', 'isbn', 'type', 'book_count',
    list_per_page = 10
    list_max_show_all = 200


@admin.register(models.Book_type)
class Book_typeAdmin(admin.ModelAdmin):
    list_display = 'type',
    ordering = 'type',


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = 'genre',
    ordering = 'genre',
