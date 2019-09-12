from django.db import models
from django.conf import settings
from django.shortcuts import reverse
import markdown
import re


class HotEvents(models.Model):
    id = models.AutoField(max_length=20, primary_key=True)
    rank = models.IntegerField('排名', default=0)
    name = models.CharField('事件名称', max_length=50)
    topic = models.CharField('话题', max_length=50)
    create_time=models.DateField(verbose_name='创建时间',auto_now_add=True)
    hot = models.CharField('热度', max_length=20)
    brief = models.CharField('事件简介', max_length=100)
    # 热点事件主页
class Event(models.Model):
    id =models.AutoField(max_length=20, primary_key=True)
    name = models.CharField('事件名称', max_length=50)
    brief = models.CharField('事件简介', max_length=100)


class Meta:
    verbose_name = '热点事件'
    verbose_name_plural = verbose_name
    ordering = ['rank']



def __str__(self):
    return self.name

def get_event_list(self):
    return HotEvents.objects.order_by("rank")
