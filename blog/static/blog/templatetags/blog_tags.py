from ..models import Category, Article
#我刚好也遇到这个问题，刚搞懂。from . import XXX 这里 “ . ”
# 的意思是你sessions当前文件夹里的初始化文件也就是sessions所在的目录下的__init__.py文件
# 。而这里面也是你sessions注册的地方。你可以打开文件目录看一下。" . "的意思有点类似命令行里面，cd ..是返回上一层目录的意思，同样，from .
# . import XXX就是从上级目录里面导入XXX

from django import template

register = template.Library();

# https://docs.djangoproject.com/en/dev/howto/custom-template-tags/
@register.simple_tag
def get_recent_article(num=5):
    return Article.objects.all().order_by('-pub_data')[1:num];

#按月归档标签
@register.simple_tag
def archives():
    return Article.objects.datas('pub_data','month',order = 'DESC');

@register.simple_tag
def get_category_tag():
    return Category.objects.all();
