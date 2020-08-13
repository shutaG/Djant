from django.db import models
from django.contrib.auth.models import AbstractUser,Permission,Group


# Create your models here.

# class baseMode(models.model):
#     update_time =

# 类的permisson应该都重写，所以应该写个公共类
class User(AbstractUser):
    email = models.CharField('邮箱', max_length=100, null=True)
    tel = models.CharField('电话', max_length=18, null=True, default=None)
    avatar = models.CharField('头像', max_length=200, null=True)

    class Meta:
        verbose_name = '管理员'
        permissions = (
            ('view_user', '查看管理员'),
            ('add_user', '添加管理员'),
            ('update_user', '修改管理员'),
            ('delete_user', '删除管理员'),
        )
        default_permissions = ()


class Menu(models.Model):
    title = models.CharField('名称', max_length=20)
    pid = models.ForeignKey("self", null=True, blank=True,  default=None,on_delete=models.SET_NULL, verbose_name="父菜单")
    type = models.CharField(choices=[('menu', '菜单'), ('permission', '权限'), ], default='menu', max_length=10)
    icon = models.CharField(max_length=50, null=True, default=None)
    path = models.CharField(max_length=50, null=True, default=None)
    component = models.CharField(max_length=50, null=True, default=None)
    premission = models.ForeignKey(Permission, null=True, default=None,on_delete=models.DO_NOTHING)
    statu = models.CharField(choices=[('hidden', '隐藏'), ('show', '显示'), ], default='show', max_length=10)
    group = models.ManyToManyField(Group,null=True, default=None)





