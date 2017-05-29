# coding:utf-8
from django.conf.urls import url

from . import views
 # name 是函数index 别名
app_name = 'blog';

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    #将对应的数字pk 放进detail便于访问
    #函数调用调用detail(request,pk)  软硬编码问题
    url(r'^article/(?P<pk>[0-9]+)/$', views.detail, name = 'detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)', views.cateory, name ='category' ),
]
