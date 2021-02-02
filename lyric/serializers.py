
from rest_framework import serializers
from .models import Lyric,Feedback

class LyricSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Lyric
        fields=('songid','albummid','title','author','album','lyric','time')

class FeedbackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Feedback
        fields=('content','time','ip')