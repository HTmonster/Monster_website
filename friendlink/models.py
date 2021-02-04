from django.db import models

class FriendLinkManager(models.Manager):
    def get_queryset(self):
        return super(FriendLinkManager,self).get_queryset().filter(visible=True)

# 友链申请
class FriendLink(models.Model):
    link=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    type=models.CharField(max_length=200)
    desc=models.CharField(max_length=500)
    visible=models.BooleanField(default=False)
    time_create = models.DateTimeField(auto_now_add=True)  # 创建时间

    #管理器
    objects = models.Manager()  # 普通
    passed  = FriendLinkManager() #通过审核的友链

    def __str__(self):
        return "友链 {}".format(self.name)
