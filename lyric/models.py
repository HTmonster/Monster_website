from django.db import models

# Create your models here.

class Lyric(models.Model):
    id = models.AutoField(primary_key=True)
    songid   =  models.IntegerField(default=-1)
    albummid =  models.CharField(max_length=100,default="")
    title    =  models.CharField(max_length=200,default="")
    author   =  models.CharField(max_length=200,default="")
    album    =  models.CharField(max_length=100,default="")
    lyric    =  models.CharField(max_length=1000,default="")
    time     =  models.CharField(max_length=100,default="")

    def __str__(self):
        return "歌词 {}".format(self.lyric)
class Feedback(models.Model):
    '''反馈的信息'''
    id       = models.AutoField(primary_key=True)
    content  = models.CharField(max_length=20400,default="")
    time     = models.CharField(max_length=500,default="")
    ip       = models.CharField(max_length=200,default="")

    def __str__(self):
        return "反馈信息 "