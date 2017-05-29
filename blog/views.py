# coding:utf-8
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
#https://stackoverflow.com/questions/29982556/from-import-models-works-but-import-models-doesnt解释为什么是.model 与搜索路径有关
from .models import Article, Category
import pygments
import markdown


def index(request):
    #return HttpResponse('欢迎访问');
    #路径 应当是setting.py 中 dir 加上下面的路径
    '''return render(request, 'blog/index.html', context = {
        'title':'我的博客首页',
        'welcome':'欢迎访问博客首页'
    })'''
    article_list = Article.objects.all().order_by('-pub_data');

    return render(request, 'blog/index.html',context = {
        'article_list' : article_list
    });

'''def detail(request,pk):
    # 如果对应的文章存在就给article  否则false  这里必须制定pk=pk  否则会报错  def get_object_or_404(klass, *args, **kwargs):
    article = get_object_or_404(Article, pk=pk);
    # 使用python库 markdown codehilite代码高亮  toc生成目录
    # article.body = markdown.markdown(article.body,
     #                                extensions = ['markdown.extensions.extra',
      #                                             'markdown.extensions.codehilite',
       #                                            'markdown.extensions.toc',
    #]
    #)
    article.body = markdown.markdown(article.body,
                                    extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'blog/detail.html', context={'article': article});
'''
def detail(request, pk):
        article = get_object_or_404(Article, pk=pk)
        article.body = markdown.markdown(article.body,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ])
        return render(request, 'blog/detail.html', context={'article': article})

# Create your views here.
def archives(request, year, month):
    #注意这pub_data__year有两个__ 由于django原因 所以用__  注意等于
    article_list = Article.objects.filter(pub_data__year = year,
                                          pub_data__month = month
                                          ).order_by('-pub_data');
    return render(request, 'blog/index.html', context={'article_list':article_list});
#  注意这里是小写
def cateory(request, pk):
    cate = get_object_or_404(Category, pk=pk);
    article_list = Article.objects.filter(category = cate).order_by('-pub_data');
    return render(request, 'blog/index.html', context = {'article_list':article_list});
