from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Lyric,Feedback
from .serializers import LyricSerializer,FeedbackSerializer
import time


@api_view(['GET'])
def lyric(request,kword):
    '''
    查询包含着kword的歌词信息
    '''
    if not kword:
        # 没有输入要搜索的单词
        return Response({"status":"Error","Msg":"No word"},status.HTTP_200_OK)
    else:
        # 之后查询部分包含的句子
        lyrics_querys= list(Lyric.objects.filter(lyric__contains=kword))


        #同首歌去重
        titles,lyrics=[],[]
        for q in lyrics_querys:
            if q.title not in titles:
                lyrics.append(q)
                titles.append(q.title)

        # 进行排序
        lyrics.sort(key=lambda x: len(x.lyric))



        if len(lyrics)>100:
            lyrics=lyrics[:100]
        # 序列化s
        serializer=LyricSerializer(lyrics,many=True)

        # 返回结果
        return Response({"status":"OK","Msg":"OK","data":serializer.data},status.HTTP_200_OK)


@api_view(['POST'])
def feedback(request):
    print("=============================")
    data=request.data
    data['ip']=request.get_host()
    data['time']=time.asctime()
    print(data)

    serializer = FeedbackSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status":"OK","Msg":"OK"}, status=status.HTTP_201_CREATED)
    return Response({"status":"Error","Msg":"Not valid"}, status=status.HTTP_400_BAD_REQUEST)