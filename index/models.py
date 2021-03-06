from django.db import models
from django.utils import timezone

class Message(models.Model):
    ''' 首页用户留言 '''

    name=models.CharField(max_length=200)
    email=models.EmailField()
    body=models.TextField(max_length=1000)
    create = models.DateTimeField(default=timezone.now)  # 创建的时间

    # 根据创建时间降序排序
    class Meta:
        ordering = ('-create',)

    # 显示设置
    def __str__(self):
        return self.name + str(self.create)




# 统计访问
class ReqLog(models.Model):
    ip     = models.CharField(max_length=100) # ip信息
    refere = models.CharField(max_length=300) # refere信息
    time   = models.DateTimeField(default=timezone.now)  # 提交时间
