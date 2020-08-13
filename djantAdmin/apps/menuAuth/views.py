# from rest_framework import viewsets
from rest_framework import views,viewsets
from rest_framework.response import Response
from menuAuth import serializer
from menuAuth import models

class Nav(views.APIView):
    true = True
    false = False
    nav = [{
      'name': 'dashboard',
      'parentId': 0,
      'id': 1,
      'meta': {
        'icon': 'dashboard',
        'title': '仪表盘',
        'show': true
      },
      'component': 'RouteView',
      'redirect': '/dashboard/workplace'
    },
    {
      'name': 'workplace',
      'parentId': 1,
      'id': 7,
      'meta': {
        'title': '工作台',
        'show': true
      },
      'component': 'Workplace'
    },
    {
      'name': 'monitor',
      'path': 'https://www.baidu.com/',
      'parentId': 1,
      'id': 3,
      'meta': {
        'title': '监控页（外部）',
        'target': '_blank',
        'show': true
      }
    },
    {
      'name': 'Analysis',
      'parentId': 1,
      'id': 2,
      'meta': {
        'title': '分析页',
        'show': true
      },
      'component': 'Analysis',
      'path': '/dashboard/analysis'
    },
    {
      'name': 'form',
      'parentId': 0,
      'id': 10,
      'meta': {
        'icon': 'form',
        'title': '表单页'
      },
      'redirect': '/form/base-form',
      'component': 'PageView'
    },
    {
      'name': 'basic-form',
      'parentId': 10,
      'id': 6,
      'meta': {
        'title': '基础表单'
      },
      'component': 'BasicForm'
    },
    {
      'name': 'step-form',
      'parentId': 10,
      'id': 5,
      'meta': {
        'title': '分步表单'
      },
      'component': 'StepForm'
    },
    {
      'name': 'aut',
      'parentId': 10,
      'id': 4,
      'meta': {
        'title': '高级表单'
      },
      'component': 'AdvanceForm'
    },
    {
        'name': 'auth',
        'parentId': 0,
        'id': 100,
        'meta': {
            'icon': 'dashboard',
            'title': '权限管理',
            'show': true,
            'type': 'menu'
        },
        'component': 'PageView',
        'redirect': '/'
    },
    {
      'name': 'authMenu',
      'parentId': 100,
      'id': 1000,
      'meta': {
        'title': '菜单管理',
        'statu': 'show',
        'type': 'menu'
      },
      'component': 'AuthMenu'
    },
    {
        'name': 'authMenu2',
        'parentId': 100,
        'id': 1001,
        'meta': {
            'title': '查看菜单',
            'statu': 'hidden',
            'type': 'permission'
        }
    }
    ]
    def get(self,request):
        data = {
            'status': '''11111''',
            'msg': 'data_msg',
            'result':self.nav
        }

        return Response(data)

from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
# 菜单管理
class Menu(viewsets.ModelViewSet):
    queryset = models.Menu.objects.all()
    serializer_class = serializer.MenuSerializer
    filter_fields = ('type',)
    filter_backends = [filters.OrderingFilter,DjangoFilterBackend]
    ordering_fields = ('id')
