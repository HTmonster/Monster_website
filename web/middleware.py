from django.utils.deprecation import MiddlewareMixin

from index.models import ReqLog

class Reqmiddle(MiddlewareMixin):

    # 统计request信息
    def process_request(self, request):
        request_ip     = request.META.get("HTTP_X_FORWARDED_FOR") if request.META.get("HTTP_X_FORWARDED_FOR") else request.META.get("REMOTE_ADDR")
        request_refere = request.META.get("HTTP_REFERER") if request.META.get("HTTP_REFERER") else ''

        reqlog = ReqLog.objects.create(ip=request_ip,refere=request_refere)
