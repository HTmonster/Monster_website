from django.contrib import admin

# Register your models here.
from .models import FriendLink



class FriendLinkAdmin(admin.ModelAdmin):
    list_display = ('name','link','type','desc')
    list_filter = ('name','link','type','desc','visible')
    search_fields = ('name','link','type','desc')
    date_hierarchy = ('time_create')
    ordering = ['name',]

admin.site.register(FriendLink,FriendLinkAdmin)
