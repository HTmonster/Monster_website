from django.contrib import admin

# Register your models here.
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('name','email','body')
    list_filter = ('create','name','email')
    search_fields = ('name','email')
    date_hierarchy = 'create'
    ordering = ['create',]



admin.site.register(Message,MessageAdmin)