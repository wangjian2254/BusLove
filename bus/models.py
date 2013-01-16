#coding=utf-8
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Person(models.Model):
    #用户个人信息
    user=models.OneToOneField(User,verbose_name=u'登录账户')
    head=models.IntegerField(default=0,verbose_name=u'默认头像')
    head_Image=models.CharField(max_length=100,verbose_name=u'头像')

class GuanZhu(models.Model):
    #关注
    user=models.ForeignKey(User,related_name=u'user',verbose_name=u'关注发起')
    guanzhu_user=models.ForeignKey(User,related_name=u'guanzhu',verbose_name=u'关注发起')

class City(models.Model):
    #城市
    name=models.CharField(max_length=10,verbose_name=u'城市名称')

class UserWord(models.Model):
    # 类似于 qq的说说
    user=models.ForeignKey(User,verbose_name=u'登录用户')
    word=models.CharField(max_length=200,verbose_name=u'说说')
    create_Time=models.DateTimeField(auto_created=True,verbose_name=u'发布时间')
    is_del=models.BooleanField(default=False,verbose_name=u'是否删除')

class Group(models.Model):
    #小组 类似豆瓣
    auther=models.ForeignKey(User,verbose_name=u'登录用户')
    name=models.CharField(max_length=50,verbose_name=u'小组名称')


class Album(models.Model):
    #相册
    user=models.ForeignKey(User,blank=True,null=True,verbose_name=u'登录用户')
    group=models.ForeignKey(Group,blank=True,null=True,verbose_name=u'小组相册')
    name=models.CharField(max_length=30,verbose_name=u'相册名称')
    type=models.IntegerField(default=0,verbose_name=u'相册类型')
    last_update=models.DateTimeField(auto_now=True,verbose_name=u'最后一次修改时间')
    is_del=models.BooleanField(default=False,verbose_name=u'是否删除')

class Image(models.Model):
    #照片
    user=models.ForeignKey(User,verbose_name=u'上传照片的用户')
    name=models.CharField(max_length=50,null=True,blank=True,verbose_name=u'图片标题')
    desc=models.CharField(max_length=150,null=True,blank=True,verbose_name=u'图片简介')
    litte=models.CharField(max_length=100,verbose_name=u'小图')
    middel=models.CharField(max_length=100,verbose_name=u'中图')
    big=models.CharField(max_length=100,verbose_name=u'大图')
    pic=models.CharField(max_length=100,verbose_name=u'原图')
    create_date=models.DateTimeField(auto_created=True)
    is_del=models.BooleanField(default=False,verbose_name=u'是否删除')


class Subject(models.Model):
    #话题
    user=models.ForeignKey(User,verbose_name=u'登录用户')
    city=models.ForeignKey(City,verbose_name=u'话题所在城市')
    group=models.ForeignKey(Group,null=True,blank=True,verbose_name=u'隶属小组',help_text=u'如果为空，那就是全站性质的')
    title=models.CharField(max_length=200,verbose_name=u'标题')
    paper=models.TextField(verbose_name=u'话题内容')
    create_date=models.DateTimeField(auto_created=True)
    is_del=models.BooleanField(default=False,verbose_name=u'是否删除')

class Replay(models.Model):
    #回复
    user=models.ForeignKey(User,verbose_name=u'回复人')
    subject=models.ForeignKey(Subject,null=True,blank=True,verbose_name=u'话题')
    image=models.ForeignKey(Image,null=True,blank=True,verbose_name=u'话题')
    content=models.CharField(max_length=500,verbose_name=u'回复内容')
    index=models.IntegerField(default=1,verbose_name=u'楼层')
    fatherid=models.ForeignKey('Replay',null=True,blank=True,verbose_name=u'对回复的回复')
    create_date=models.DateTimeField(auto_created=True)
    is_del=models.BooleanField(default=False,verbose_name=u'是否删除')

class BusLine(models.Model):
    #公交线路
    city=models.ForeignKey(City,verbose_name=u'公交路线隶属城市')
    name=models.CharField(max_length=20,verbose_name=u'公交名称')
    group=models.ForeignKey(Group,verbose_name=u'指向小组')


class BusSite(models.Model):
    #公交站台
    city=models.ForeignKey(City,verbose_name=u'公交路线隶属城市')
    name=models.CharField(max_length=20,verbose_name=u'公交站名称')
    group=models.ForeignKey(Group,verbose_name=u'指向小组')

class BusLineSite(models.Model):
    #公交线路各个站点
    FANGXIANG=( (0,'上行'),
                (1,'下行'),
                (2,'环线'))
    busline=models.ForeignKey(BusLine,verbose_name=u'隶属于哪条公交')
    bussite=models.ForeignKey(BusSite,verbose_name=u'公交站牌')
    type=models.IntegerField(default=0,choices=FANGXIANG,verbose_name=u'方向')
    index=models.CharField(max_length=5,verbose_name=u'排序')
    is_del=models.BooleanField(default=False,verbose_name=u'是否废除')





