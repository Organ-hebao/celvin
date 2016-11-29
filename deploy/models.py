#coding:utf-8
# from __future__ import unicode_literals

from django.db import models
from server.models import *

class Application(models.Model):
    id = models.AutoField(primary_key=True)
    appName = models.CharField(max_length=50) # 应用名称
    appDesc = models.CharField(max_length=50) # 应用描述
    appHost = models.ForeignKey(Instance)  # 应用主机
    appDir = models.CharField(max_length=50)  # 应用目录
    iisName = models.CharField(max_length=50) # IIS名称



