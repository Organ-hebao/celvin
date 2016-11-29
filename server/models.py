#coding:utf-8
from __future__ import unicode_literals

from django.db import models

class Instance(models.Model):
    id = models.AutoField(primary_key=True)
    instanceName = models.CharField(max_length=50) # 实例名称
    lanIp = models.GenericIPAddressField() # 内网IP
    wanIpSet = models.GenericIPAddressField()
    os = models.CharField(max_length=30)
    zoneName = models.CharField(max_length=30)



