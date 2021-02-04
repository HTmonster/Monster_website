import time

from django.db import models
from django.urls import reverse
from django.utils import timezone
from mdeditor.fields import MDTextField
from taggit.managers import TaggableManager
from uuslug import slugify


# 一篇文章
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)  # 文章标题
    body = MDTextField()  # 文章主体 markdown
    views_nums = models.PositiveIntegerField(default=0)  # 阅读次数

    time_publish=models.DateTimeField(default=timezone.now) # 提交时间
    time_create=models.DateTimeField(auto_now_add=True)     # 创建时间
    time_update=models.DateTimeField(auto_now=True)         # 更新时间

    tag = TaggableManager()  # 文章标签
    url_slug = models.SlugField(editable=False, max_length=200)  # slug 自动生成

    objects = models.Manager()  # 普通

    # 根据发布时间进行降序排序
    def save(self, *args, **kwargs):
        self.url_slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering=('-time_publish',)

    #重写str函数
    def __str__(self):
        return self.title

    #获得绝对路径
    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[self.url_slug])

    #阅读量增加
    def increase_view(self):
        self.views_nums+=1
        self.save(update_fields=['views_nums'])

#评论
class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    body=models.TextField(default="")
    user_id = models.PositiveIntegerField()
    time_create=models.DateTimeField(auto_now_add=True)
    time_update=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    class Meta:
        ordering=('-time_create',)

    def __str__(self):
        return 'Comment {} by',format(self.body)