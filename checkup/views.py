#-*- encoding: utf-8 -*-
from django.shortcuts import render
from Car.forms import TestDriveForm
from Car.models import Car
from testdrive.models import TestDrive
from django.contrib.auth.models import User,auth
from django.shortcuts import render_to_response, redirect,HttpResponse
from django.core.context_processors import csrf
from .models import TypeOfService, Checkup
# Create your views here.

def add_checkup(request):
    args={}
    args.update(csrf(request))
    args['service'] = TypeOfService.objects.all()
    args['car'] = TypeOfService.objects.all()
    if request.POST:
        de=Checkup(date_completed= request.POST.get('date_completed',''),
                   reg_number=request.POST.get('reg_number',''),
                   run=request.POST.get('run',''),
                   car=request.POST.get('marka',''),
                   type_of_service=TypeOfService.objects.get(id=request.POST.get('type_of_service','')),
                   user=User.objects.get(id= auth.get_user(request).id)
                   )
        de.save()
        args['word'] = "Спасибо за запись на техосмотр!"
    args['username'] = auth.get_user(request).username
    return render_to_response('checkup.html',args)

def delete_checkup(request,id_service):
    args={}
    args.update(csrf(request))
    de = Checkup.objects.get(id=id_service)
    de.delete()
    return redirect('/order/cart/')