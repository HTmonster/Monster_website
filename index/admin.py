from django.contrib import admin

# Register your models here.
from .models import Message,ReqLog

class ReqLogAdmin(admin.ModelAdmin):
    list_display = ('ip','refere','time')
    list_filter = ('ip','refere','time')
    search_fields = ('ip','refere')
    date_hierarchy = 'time'
    ordering = ['time',]


class MessageAdmin(admin.ModelAdmin):
    list_display = ('name','email','body')
    list_filter = ('create','name','email')
    search_fields = ('name','email')
    date_hierarchy = 'create'
    ordering = ['create',]


admin.site.register(ReqLog,ReqLogAdmin)
admin.site.register(Message,MessageAdmin)