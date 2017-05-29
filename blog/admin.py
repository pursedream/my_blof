from django.contrib import admin
from .models import Article,Tag,Category
# Register your models here.
# 逻辑错误  是文章属于某个分类下，，所以下面这种方法不合适
'''
class TagInline(admin.StackedInline):
    model = Tag;

class Category_Inline(admin.StackedInline):
    model = Category;

class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagInline,Category_Inline];
'''

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields' : ['title']}),
        ('Data information',    {'fields' : ['pub_data']}),
        ('Abstract',            {'fields' : ['abstract']}),
        (None,                  {'fields' : ['body']}),
        (None,                  {'fields' : ['tag']}),
        ('Category',            {'fields' : ['category']}),
        (None,                  {'fields' : ['user']}),
    ]
    list_display = ('title','pub_data','category','user');
 #   list_filter = ['pub_data'];
    list_filter = ['pub_data','category'];
    search_fields = ['title'];

admin.site.register(Article,ArticleAdmin);

admin.site.register(Tag);

admin.site.register(Category);
