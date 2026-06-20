from django.contrib import admin
from .models import Category, Tag, Task

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_completed', 'category', 'created_at')
    list_filter = ('is_completed', 'category')
    search_fields = ('title', 'description')
