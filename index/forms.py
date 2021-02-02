from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    ''' 首页留言表单 '''
    class Meta:
        model=Message
        fields=('name','email','body')