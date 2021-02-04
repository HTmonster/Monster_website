def show_userinfo(request):

    context={} #上下文

    #用户的信息
    user=request.user
    if user and user.is_authenticated:
        #用户存在 并已经登录
        context['user']=user
    return context