from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import lyric,feedback



urlpatterns = [
    url(r'^lyric/(\w+)/$',lyric),
    url(r'^feedback/$',feedback),
]
