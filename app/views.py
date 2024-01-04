from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *

def htmlfiles(request):
    if request.method=='POST':
        username=request.POST['un']
        return HttpResponse(username)

    return render(request,'htmlfiles.html')


def create_school(request):
    if request.method=='POST':
        sn=request.POST['sn']
        sl=request.POST.get['sl']
        sp=request.POST.get['sp']
        SO=school.objects.get_or_create(Sname=sn,Slocation=sl,Sprincipal=sp)[0]
        SO.save()

        return HttpResponse('data is created')
    return render(request,'create_school.html')