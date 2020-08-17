from django.urls import  path

from common import views

urlpatterns=[
    path('uploadkey/', views.Qiniu.as_view()),
]