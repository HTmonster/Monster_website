from django.contrib import messages
from django.core.mail import mail_admins
from django.shortcuts import render

from .forms import FriendLinkForm
from .models import FriendLink


def friendlink(request):

    # 审核通过的友链
    friendlinks=FriendLink.passed.all()

    if request.method == 'POST':
        friendlink_from=FriendLinkForm(data=request.POST)

        if friendlink_from.is_valid():
            friendlink_from.save()
            messages.success(request, "提交成功!! 感谢您的支持")
            # 发送给管理员信息
            subject = "新友链申请! 来自[{} {}]".format(friendlink_from['name'].value(), friendlink_from['link'].value())
            message = "类型 {}\n 描述 {}".format(friendlink_from['type'].value(), friendlink_from['desc'].value())
            mail_admins(subject, message, fail_silently=True)
        else:
            messages.warning(request, "抱歉，似乎出了点错误。")

    return render(request,'friendlink/friendlink.html',context={'friendlinks':friendlinks})