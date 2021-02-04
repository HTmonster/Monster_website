
from django.conf.urls import url
from django.urls import path, re_path
from .import views

app_name="oauth"

urlpatterns = [
    re_path(r'^github/$', views.GitHubOAuthView.as_view(), name='github_oauth'),
    path('github_login/',views.github_login,name="github_login"),
    # url(r'/github/$',views.github,name="github"),
]