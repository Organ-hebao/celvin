from django.shortcuts import render
from django.shortcuts import render_to_response

def listApps(request):
     return render_to_response("deploy/deploy_list.html",locals())


def addApps(request):
     return render_to_response("deploy/deploy_add.html",locals())