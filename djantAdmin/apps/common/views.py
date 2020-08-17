from rest_framework.views import APIView
from rest_framework.response import Response
from qiniu import Auth
from utils.response import SimResponse
from django.conf  import settings

# 七牛云相关
class Qiniu(APIView):
    def get(self, request):
        AK = settings.QINIU_AK
        SK = settings.QINIU_SK
        DOMAIN = settings.QINIU_DOMAIN
        qinu = Auth(AK, SK)



        # 前端上传后,返回给前端的格式
        returnBody = '{"name": $(key), "src":"%s/$(key)" , "w": $(imageInfo.width), "h": $(imageInfo.height)}'%(DOMAIN)
        policy = {
            'returnBody':returnBody
        }
        # 要上传到的空间
        bucket_name = 'djant'
        token = qinu.upload_token(bucket_name, expires=3600,policy=policy)
        return SimResponse(token)
