from django.contrib import admin

# Register your models here.

from .models import Post,Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','url_slug','time_publish')
    list_filter = ('time_create','time_publish')
    search_fields = ('title','body')
    date_hierarchy = 'time_publish'
    ordering = ['time_publish']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('body','time_create')
    list_filter = ('active','post')
    search_fields = ('post',)
    date_hierarchy = 'time_create'
    ordering = ['active','time_create']


admin.site.register(Comment,CommentAdmin)
admin.site.register(Post,PostAdmin)