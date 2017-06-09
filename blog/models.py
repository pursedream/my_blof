# coding:utf-8
#由于中文注释，强调编码方式
from django.db import models
#内置应用，用来处理网站用户注册登录
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Tag(models.Model):

    name = models.CharField(max_length=100);

    #解释其显示下面函数内容 便于观察
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100);

    def __str__(self):
        return self.name;

class Article(models.Model):
    pub_data = models.DateTimeField();
    abstract = models.CharField(max_length=300, blank=True);
    #charfield 必须存入数据适合较短的， textfield适合较长的
    title = models.CharField(max_length=100);
    body = models.TextField();
    #http://www.cnblogs.com/linxiyue/p/3667418.html 对应关系
    category = models.ForeignKey(Category);
    tag = models.ManyToManyField(Tag);
    #有的时候这一句为tag = models.ForeignKey(Category, on_delete = models.CASCADE)

    user = models.ForeignKey(User);
    
    def __str__(self):
        return self.title;
#解析域名  blog:detail urls中指定的detail函数  在index中调用该函数/article/pk  软硬编码
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk':self.pk});
