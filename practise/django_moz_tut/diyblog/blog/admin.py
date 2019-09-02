from django.contrib import admin
from .models import Blog, BlogAuthor, BlogComment


# Register your models here.
admin.site.register(Blog)
admin.site.register(BlogAuthor)
admin.site.register(BlogComment)

"""
class BlogAuthorInline(admin.TabularInline):
    model = BlogAuthor

class BlogAuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')
    inlines = [BlogAuthorInline]

admin.site.register(BlogAuthor, BlogAuthorInline)
"""