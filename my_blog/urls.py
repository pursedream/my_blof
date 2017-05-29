"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

#该文件下一般放整改工程的url配置 我们可以选择放在自己的应用中,同时为了识别这句话 需要在猪url加入include语句
from django.conf.urls import url, include
from django.contrib import admin
# from . import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
# 识别blog下的urls， 注意下面写法,如果是r'blog'，则url会是blog/...
    url(r'',include('blog.urls')),
  #  url(r'^$', views.index, name = 'index'),
]
