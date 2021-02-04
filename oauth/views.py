import requests
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages

from web import settings
from oauth.models import Profile


class OAuthView(View):
    '''通用 Oauth 认证'''

    access_token_url = None
    user_api = None
    client_id = None
    client_secret = None

    def get(self,request,*args,**kwargs):
        access_token=self.get_access_token(request)
        user_info=self.get_user_info(access_token)
        # 在子类中实现authenticate()方法
        return self.authenticate(user_info)

    def get_access_token(self,request):
        ''' 获得 access token'''
        url=self.access_token_url

        headers={'Accept':'application/json'}
        data={
            'client_id':self.client_id,
            'client_secret':self.client_secret,
            'code':request.GET['code']
        }

        #发起请求
        res=requests.post(url,data,headers=headers)

        #解析返回参数
        res_json=res.json()


        if 'access_token' in res_json:
            return res_json['access_token']
        else:
            #code 过期  返回403
            raise PermissionDenied
    def get_user_info(self,access_token):
        ''' 获取用户的信息 '''
        headers={
            'Authorization':"token "+access_token
        }
        url=self.user_api

        #请求
        res=requests.get(url,headers=headers)
        #提取用户信息
        user_info=res.json()

        return user_info

    def get_success_url(self):
        '获取登录成功后返回的网页'
        if 'next' in self.request.session:
            # 还记得在OAuthLoginView中保存到session里的next吗
            return self.request.session.pop('next')
        else:
            # 没有next就只能返回主页
            return '/'

class GitHubOAuthView(OAuthView):
    'github账号认证视图'
    # 在具体类中定义相应的参数
    access_token_url = 'https://github.com/login/oauth/access_token'
    user_api = 'https://api.github.com/user'
    client_id = settings.GITHUB_CLIENT_ID
    client_secret = settings.GITHUB_CLIENT_SECRET

    def authenticate(self, user_info):
        '用户认证'
        user = User.objects.filter(profile__github_id=user_info['id'])
        if not user:
            # 用户的模型见下文
            # user_info里'login'为用户名，'id'为GitHub的id，'avatar_url'为用户头像的url
            # 除此还有很多其他信息，如果想知道，直接print(user_info)
            user = User.objects.create_user(user_info['login'])
            profile = Profile(
                user=user,
                github_id=user_info['id'],
                avatar=user_info['avatar_url'],
                avatar_url=user_info['avatar_url']
            )
            profile.save()
        else:
            user = user[0]
        # 用login函数登录，logout函数注销
        login(self.request, user)
        return redirect(self.get_success_url())

def github_login(request):
    ''' github 登录'''

    if request.method=='GET':
        request.session['next']=request.META.get('HTTP_REFERER','/')

        url=settings.GITHUB_AUTHORIZE_URL+"?client_id="+settings.GITHUB_CLIENT_ID

        return HttpResponseRedirect(url)
