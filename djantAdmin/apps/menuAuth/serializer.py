from rest_framework import serializers
from menuAuth import models
from django.contrib.auth.password_validation import validate_password

class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model =models.Menu
        fields = ['id','type','title','icon','component','statu','path','pid','premission_id']
        # extra_kwargs = {
        #     ''
        # }


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ['id','first_name','username','tel','email','avatar','is_active','password']
        extra_kwargs = {
            'id':{
                'read_only':True
            },
            'passsword':{
                'write_only':True
            }
        }

    def validate(self, attrs):
        from django.contrib.auth.hashers import (make_password)
        attrs['password'] = make_password(attrs['password'])
        return  attrs

    # def create(self,validated_data):
    #
    #     username = 'jhon1'
    #     password = 'lggg1234'
    #     from django.contrib.auth.hashers import (
    #         make_password,
    #     )
    #     print('密码',make_password('lggg1234'))
    #     # email = '648949076@qq.com'
    #     # user = models.User.objects.create_user(username, email, password)
    #     # user.first_name = '刘刚刚'
    #     # user.save()
    #     #
    #     # data = {
    #     #     'result':111
    #     # }
    #     # return data