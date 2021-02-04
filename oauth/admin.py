from django.contrib import admin

# Register your models here.
from .models import Profile



class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','avatar_url','github_id')
    list_filter = ('user',)
    search_fields = ('user','github_id')


admin.site.register(Profile,ProfileAdmin)