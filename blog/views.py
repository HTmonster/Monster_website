import datetime

import markdown
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import  messages
from django.views.generic import ListView,View

from django.utils.text import slugify
from markdown.extensions.toc import TocExtension

from .forms import CommentForm
from .models import Post
from taggit.models import Tag


#文章列表页
class PostListView(ListView):

    model=Post
    template_name="blog/post_list.html"
    context_object_name="Posts"
    paginate_by=8 #分页数据量

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)

        # 添加自定义的参数
        context['post_count']=Post.objects.all().count()
        context['tags']=Tag.objects.all()
        context['top_posts']=Post.objects.all().order_by('-views_nums')[:5]


        #计算分页显示的范围
        current_page,nums=context['page_obj'].number,context['paginator'].num_pages
        range_s=current_page-3 if current_page>3 else 0
        range_e=range_s+5 if range_s+5<nums else nums
        context['front_5_page']=current_page-5 if current_page>5 else None #向前5页
        context['back_5_page']= current_page+5 if current_page<nums-5 else None #向后5页
        context['page_range']=list(context['paginator'].page_range)[range_s:range_e]#显示范围

        tag=self.request.GET['tag'] if "tag" in self.request.GET.dict().keys() else None

        #分页跳转url 兼容tag
        context['pagination_url']="?tag={}&page=".format(tag) if tag else "?page="

        return context


    def get_queryset(self):
        #只返回发布的文章

        if "tag" in self.request.GET.dict().keys():
            Posts=Post.objects.filter(tag__name__in=[self.request.GET['tag']])
            messages.success(self.request,"标签 "+self.request.GET['tag']+" 共有"+str(Posts.count())+"条")
            return Posts
        else:
            return Post.objects.all()


# 文章详情
def post_detail(request,slug):

    post        = get_object_or_404(Post,url_slug=slug)# 文章
    comments    = post.comments.filter(active=True)    # 评论

    # 评论获取用户头像
    for comment in comments:
        comment.user = User.objects.get(id=comment.user_id)

    # 评论分页
    paginator = Paginator(comments, 4)

    page = request.GET.get('page')
    try:
        comment_1_page = paginator.page(page)
    except:
        comment_1_page = paginator.page(1)

    # ajax 动态请求评论分页
    if request.is_ajax():
        data = {
            'current_url': request.path,
            'comments': comment_1_page,
            'comments_page_nums': range(1, comment_1_page.paginator.num_pages + 1)
        }

        return render(request, 'blog/post_comments.html', data)
    # 正常访问
    else:
        post.increase_view() # 增加访问数

        # 文章内容markdown 渲染
        md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite', #代码高亮扩展
                TocExtension(baselevel='1',slugify=slugify),# 摘要
                'markdown.extensions.tables'])
        post.body=md.convert(post.body)
        post.toc =md.toc

        # 类似文章 和主tag一致
        similar_posts = Post.objects.filter(tag__in=post.tag.values_list('id')[0] if post.tag.values_list('id') else []).order_by('-views_nums')
        similar_posts = similar_posts.exclude(id=post.id)
        similar_posts = similar_posts[:5]

        # 最近发布(6周内）
        ten_weeks_ago=datetime.date.today()-datetime.timedelta(weeks=6)
        recent_posts = Post.objects.filter(time_update__gte=ten_weeks_ago).order_by('time_update').exclude(id=post.id)
        recent_posts = recent_posts[:5]

        # 评论提交
        if request.method == 'POST':

            comment_form = CommentForm(data=request.POST)

            # 表单有效
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.post = post
                new_comment.user_id = request.user.id
                new_comment.save()
                messages.success(request, "您的评论提交成功")
                # 向管理员发送消息
            else:
                messages.error(request, "抱歉，似乎有点错误。。")

        else:
            comment_form=CommentForm()


        context = {
            'post': post,
            'current_url': request.path,

            'comment_form': comment_form,
            'comments': comment_1_page,
            'comments_total': len(comments),
            'comments_page_nums': range(1, comment_1_page.paginator.num_pages + 1),

            'similar_posts': similar_posts,
            'recent_posts': recent_posts
        }

    return render(request,'blog/post.html',context)

# 文章归档
def archive(request):

    archive_posts=Post.objects.values('time_publish','title','url_slug')

    return  render(request,'blog/archive.html',{'archive_posts':archive_posts})