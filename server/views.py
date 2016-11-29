#coding:utf-8
from django.shortcuts import HttpResponse
from qcloudapi.QcloudApi.qcloudapi import QcloudApi
from server.models import Instance
from celvin.api import *
from django.shortcuts import render_to_response
import json

def getInstances(request):
    module = 'cvm'
    action = 'DescribeInstances'

    config = {
        'Region':'shjr',

        'method':'get'
    }

    params = {

    }

    try:
        service = QcloudApi(module, config)

        # 调用接口，发起请求
        instances = service.call(action, params)
        instances_json = json.loads(instances)
        instanceSet = instances_json['instanceSet']
        instances_length = len(instanceSet)
        print instances_length
        for i in xrange(0,instances_length):
            instanceName = instanceSet[i]['instanceName']
            lanIp = instanceSet[i]['lanIp']
            wanIpSet = instanceSet[i]['wanIpSet']
            os = instanceSet[i]['os']
            zoneName = instanceSet[i]['zoneName']
            is_existe = Instance.objects.filter(lanIp=lanIp)
            if is_existe:
                Instance.objects.filter(lanIp=lanIp).update(instanceName = instanceName,lanIp = lanIp,
                                        wanIpSet = wanIpSet,os = os,zoneName = zoneName)
            else:
                qs = Instance()
                qs.instanceName = instanceName
                qs.lanIp = lanIp
                qs.wanIpSet = wanIpSet
                qs.os = os
                qs.zoneName = zoneName
                qs.save()
    except Exception,e:
        print 'exception',e
    loginfo("Successful acquisition of qcloud instances")
    return HttpResponse("成功获取腾讯云服务器信息")

def listInstance(request):
    instances = Instance.objects.all()
    return render_to_response("server/server_list.html",locals())











