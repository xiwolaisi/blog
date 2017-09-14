from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible

# Create your models here.
class Category(models.Model):
    #分类
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Tag(models.Model):
    #标签
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Post(models.Model):
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})
    #标题
    title = models.CharField(max_length=100)
    #正文
    body = models.TextField()
    #创建时间
    create_time = models.DateTimeField()
    #最后修改时间
    modified_time = models.DateTimeField()
    #文章摘要
    excerpt = models.CharField(max_length=200,blank=True)
    #分类
    category = models.ForeignKey(Category)
    #标签
    tags = models.ManyToManyField(Tag,blank=True)
    #作者
    author = models.ForeignKey(User)
    class Meta:
        ordering = ['-create_time']
