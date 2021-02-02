from django.contrib import messages
from django.shortcuts import render

# Create your views here.

from .forms import MessageForm


def index(request):
    # 留言提交
    if request.method == 'POST':
        message_form = MessageForm(data=request.POST)
        print("w")
        # 如果表单有效
        if message_form.is_valid():
            new_message = message_form.save(commit=False)
            new_message.save()  # 保存
            # 全局消息回复
            messages.success(request, "留言成功!! 我将尽快联系您")
        else:
            messages.warning(request, "提交出错啦，可能格式不正确")
    else:
        message_form = MessageForm()

    return render(request, 'index/index.html', {'message_form': message_form})
