from django.contrib import admin

from blog.models import BlogWriter


# Register your models here.
@admin.register(BlogWriter)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image', 'is_published')
    list_filter = ('title',)
    search_fields = ('title', 'content')
