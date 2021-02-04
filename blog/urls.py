
from django.conf.urls import url
from django.urls import path
from .import views

app_name="blog"


urlpatterns = [
    path('archive/', views.archive, name="post_archive"),       # 文章归档
    url(r'^post/(.+)/$', views.post_detail, name="post_detail"),# 文章详情
    url('', views.PostListView.as_view(), name="post_list"),    # 文章列表
]