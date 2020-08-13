from rest_framework import serializers
from menuAuth import models

class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model =models.Menu
        fields = ['id','type','title','icon','component','statu','path','pid','premission_id']
        # extra_kwargs = {
        #     ''
        # }

