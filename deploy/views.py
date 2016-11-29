from django.shortcuts import render
from django.shortcuts import render_to_response
from server.views import Instance
from deploy.models import Application
from django.http import HttpResponseRedirect

def listApps(request):
     apps = Application.objects.all()
     return render_to_response("deploy/deploy_list.html",locals())


def addApps(request):
     if request.method == "GET":
          instances = Instance.objects.all().order_by('lanIp')
          return render_to_response("deploy/deploy_add.html",locals())
     elif request.method == "POST":
          appName = request.POST.get('appName')
          appDesc = request.POST.get('appDesc')
          appHost = request.POST.getlist('appHost')
          number = len(appHost)
          appDir = request.POST.get('appDir')
          iisName = request.POST.get('iisName')
          for i in xrange(number):
               if Application.objects.filter(appName=appName,appHost=appHost[i]):
                    print "existe"
               else:
                    host = Instance.objects.get(id=appHost[i])
                    Application(appName=appName,appDesc=appDesc,appHost=host,appDir=appDir,iisName=iisName).save()
          return HttpResponseRedirect('list_app')

