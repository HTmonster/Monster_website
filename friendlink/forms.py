from django import forms
from .models import FriendLink

class FriendLinkForm(forms.ModelForm):

    class Meta:
        model=FriendLink
        fields=('link','name','type','desc')