from rest_framework.response import Response

class SimResponse(Response):
    def __init__(self,result = [],msg = '上传成功',code = 2000 ):
        data = {
            'code':code,
            'result':result,
            'mag':msg
        }
        super().__init__(data)
